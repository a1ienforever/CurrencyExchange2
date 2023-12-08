from datetime import datetime

import requests
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QMessageBox

import converter_ui
from data import currencies_list
from bs4 import BeautifulSoup


class Converter(QMainWindow):
    # TODO: необходимо оптимизировать код

    def __init__(self):
        self.usd = None
        self.table_window = None
        self.rub = 0
        self.usd_price = 0
        self.name_bank = ''
        self.name_crypt = ''
        self.result = 0
        super(Converter, self).__init__()
        self.ui = converter_ui.Converter_MainWindow()
        self.ui.setupUi(self)
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
                price_crypt = f"{float(data_price['price']):.3f}"
                return float(price_crypt)

    def get_rub(self):
        self.rub = self.ui.input_rub.text()
        if self.rub == '':
            QMessageBox.critical(self, 'Error!', "Введите сумму для конвертации!")
        else:

            return float(self.rub)

    def convert_to_crypt(self):
        self.rub = self.get_rub()
        self.usd_price = self.parse_usd_price()
        self.name_crypt = self.request_exchange()

        self.usd = self.rub / self.usd_price
        result = self.usd / self.name_crypt
        self.result = result
        return result

    def set_result(self):
        self.convert_to_crypt()
        self.ui.output_result.setText(str(self.convert_to_crypt()))

    def get_datetime(self):
        current_datetime = datetime.now()
        formatted_datetime = current_datetime.strftime("%d.%m.%Y %H:%M")
        return formatted_datetime

    def get_result(self):
        rub = self.rub
        usd = self.usd
        crypt = self.result
        bank = self.name_bank
        date = self.get_datetime()
        return f"{date}: {rub} rub -> {usd} usd -> {crypt}{self.select_currency()} Bank: {bank}"
