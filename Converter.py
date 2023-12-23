import concurrent.futures
import sqlite3
from datetime import datetime

import requests
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt
import converter_ui
import table_main_window_ui
from Table import Table
from data import currencies_list
from bs4 import BeautifulSoup
from DataBase import DataBase


class Converter(QMainWindow):
    def __init__(self):
        self.table_item = None
        self.table = Table()
        self.table.setWindowFlag(self.table.windowFlags() | Qt.WindowStaysOnTopHint)
        self.table.show()
        self.usd = None
        self.table_window = None
        self.name_bank = ''
        self.name_crypt = ''
        self.db = DataBase()
        super(Converter, self).__init__()
        self.ui = converter_ui.Converter_MainWindow()
        self.ui.setupUi(self)
        self.db.start_database()
        self.ui.convert_button.clicked.connect(self.set_result)

    def parse_usd_price(self):
        url = 'https://www.sravni.ru/valjuty/cb-rf/usd/'
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            tags = soup.find_all('div', class_='styles_value-text__JklK4 _5gmjom')
            value = tags[1].text
            new_val = value.replace(',', '.')

            self.name_bank = tags[1].parent.find_next('a').text

            usd_price = float(new_val[0:5])
            return usd_price

    def select_currency(self):
        currency = self.ui.choose_crypt.currentText()
        return currency

    def select_exchange(self):
        currency = self.ui.choose_exchange.currentText()
        return currency

    def request_exchange(self):
        select_exchange = self.select_exchange().lower()
        select_crypt = self.select_currency().upper()
        for value in currencies_list[select_crypt]:
            if select_exchange in value:
                data_price = requests.get(
                    currencies_list[select_crypt][currencies_list[select_crypt].index(value)]).json()
                if select_exchange == "bybit":
                    price_crypt = f"{float(data_price['result']['price']):.3f}"
                    return float(price_crypt)
                if select_exchange == 'bingx':
                    price_crypt = f"{float(data_price['data']['price']):.3f}"
                    return float(price_crypt)
                else:
                    price_crypt = f"{float(data_price['price']):.3f}"
                    return float(price_crypt)

    def get_rub(self):
        rub = self.ui.input_rub.text()
        if rub == '':
            QMessageBox.critical(self, 'Error!', "Введите сумму для конвертации!")
        else:
            return int(rub)

    # TODO: создать threadpool
    def convert_to_crypt(self):
        rub = self.get_rub()
        usd_price = self.parse_usd_price()
        name_crypt = self.request_exchange()
        usd = rub / usd_price
        result = usd / name_crypt
        date_time = self.get_datetime()
        self.record_to_db(date_time, rub, usd_price, result)
        self.table_item = self.get_result(date_time, rub, usd_price, result)
        self.set_lable_text(self.name_bank)
        self.table.add_item(self.table_item)
        return result

    def set_result(self):
        string = self.convert_to_crypt()
        self.ui.output_result.setText(str(f"{string:.5f}"))

    def get_datetime(self):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%d.%m.%Y %H:%M")
        return formatted_datetime

    def get_result(self, datetime, rub, usd, crypt):
        return f"{datetime} {rub} rub -> {usd} usd -> {crypt:.5f} {self.select_currency()}"

    def record_to_db(self, datetime, rub, usd, crypt):
        with sqlite3.connect('identifier.sqlite') as db:
            cursor = db.cursor()
            cursor.execute(f"SELECT datetime FROM conversion WHERE datetime = '{datetime}'")
            if cursor.fetchone() is None:
                cursor.execute(f"INSERT INTO conversion VALUES(?,?,?,?,?)",
                               (datetime, rub, usd, crypt, self.select_currency()))
                db.commit()
                print('Запись сделана!')
            else:
                print("Error!")

    def set_lable_text(self, text):
        str = (f'Перевод в доллары выполнен через банк {text}.\n'
               f'{self.table_item}')
        self.ui.footer.setText(str)
