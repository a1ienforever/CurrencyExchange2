import requests
from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QMainWindow, QMessageBox

import converter_ui
from Table import Table
from data import currencies_list
from bs4 import BeautifulSoup

class Converter(QMainWindow):
    # TODO: необходимо оптимизировать код

    def __init__(self):
        self.table_window = None
        self.usd_price = 0
        self.bank = ''
        self.result = 0
        self.table = Table()
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

            self.bank = tags[1].parent.find_next('a').text

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
        rub = self.ui.input_rub.text()
        if rub == '':
            QMessageBox.critical(self, 'Error!', "Введите сумму для конвертации!")
        else:

            return float(rub)

    def convert_to_crypt(self):
        rub = self.get_rub()
        usd_price = self.parse_usd_price()
        crypt = self.request_exchange()

        usd = rub / usd_price
        result = usd / crypt

        return result

    def set_result(self):
        self.convert_to_crypt()
        self.ui.output_result.setText(str(self.convert_to_crypt()))
        # self.open_table_window()

    # def open_table_window(self):
    #     self.table_window = Table()
    #     self.table_window.setWindowFlag(self.table_window.windowFlags() | Qt.WindowStaysOnTopHint)
    #     self.table_window.show()
