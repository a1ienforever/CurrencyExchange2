import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from currency_exchange_ui import Ui_MainWindow
import requests
from data import currencies_list
import data


class CurrencyExchange(QMainWindow):

    def __init__(self):
        self.row = 0
        super(CurrencyExchange, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.add_currency_pair)
        self.ui.manual_update.clicked.connect(self.manual_update)

    # def parser(self):
    #     # Перенести все в массив
    #     data_binance = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT').json()
    #     data_commex = requests.get('https://api.commex.com/api/v1/ticker/price?symbol=BTCUSDT').json()
    #     price_commex = f"{float(data_commex['price']):.3f}"
    #     currency_commex = str(data_commex['symbol'])
    #     price_binance = f"{float(data_binance['price']):.3f}"
    #     currency_binance = str(data_binance['symbol'])
    #     name_exchange = 'Binance'
    #     self.ui.tableWidget.horizontalHeaderItem(0).setText(name_exchange)
    #     self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(price_binance))
    #     self.ui.tableWidget.verticalHeaderItem(0).setText(currency_binance)
    #
    #     self.ui.tableWidget.horizontalHeaderItem(1).setText('CommEX')
    #     self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(price_commex))

    def select_currency(self):
        return self.ui.box_currency.currentText()

    def set_vertical_header_item(self):
        self.ui.tableWidget.verticalHeaderItem(self.row).setText()

    def parser_binance(self, selected_currency, row):
        data_price = requests.get(currencies_list[selected_currency][0]).json()
        price = f"{float(data_price['price']):.3f}"
        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(price))

    def parser_commex(self, selected_currency, row):
        data_price = requests.get(currencies_list[selected_currency][1]).json()
        price = f"{float(data_price['price']):.3f}"
        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(price))

    def add_currency_pair(self):
        if self.row <= 2:
            selected_currency = self.select_currency()
            self.ui.tableWidget.verticalHeaderItem(self.row).setText(selected_currency)
            self.parser_binance(selected_currency, self.row)
            self.parser_commex(selected_currency, self.row)
            self.row += 1

    def manual_update(self):
        i = 0
        for key in currencies_list:
            if i < self.row:
                self.parser_binance(key, i)
                self.parser_commex(key, i)
                i += 1
            else:
                break

        # for link in currencies_list:


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyExchange()
    window.setWindowFlags(window.windowFlags() | Qt.WindowStaysOnTopHint)
    window.show()
    sys.exit(app.exec())
