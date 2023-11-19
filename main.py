import concurrent.futures
import sys
import threading
import time

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

    def request_binance(self, selected_currency, row):
        data_price = requests.get(currencies_list[selected_currency][0]).json()
        price = f"{float(data_price['price']):.3f}"
        self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(price))

    def request_commex(self, selected_currency, row):
        data_price = requests.get(currencies_list[selected_currency][1]).json()
        price = f"{float(data_price['price']):.3f}"
        self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(price))

    def request_mexc(self, selected_currency, row):
        data_price = requests.get(currencies_list[selected_currency][2]).json()
        price = f"{float(data_price['price']):.3f}"
        self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(price))

    def request_bybit(self, selected_currency, row):
        data_price = requests.get(currencies_list[selected_currency][3]).json()
        price = f"{float(data_price['result']['price']):.3f}"
        self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(price))

    def add_currency_pair(self):
        if self.row <= 10:
            selected_currency = self.select_currency()
            self.ui.tableWidget.verticalHeaderItem(self.row).setText(selected_currency)
            # start_time1 = time.time()
            #
            # # threading1 = threading.Thread(target=self.request_binance, args=(selected_currency, self.row))
            # self.request_binance(selected_currency, self.row)
            #
            # # threading2 = threading.Thread(target=self.request_commex, args=(selected_currency, self.row))
            # self.request_commex(selected_currency, self.row)
            #
            # # threading3 = threading.Thread(target=self.request_mexc, args=(selected_currency, self.row))
            # self.request_mexc(selected_currency, self.row)
            #
            # # threading4 = threading.Thread(target=self.request_bybit, args=(selected_currency, self.row))
            # self.request_bybit(selected_currency, self.row)
            #
            # end_time1 = time.time()
            #
            # print(f'Time1: {end_time1 - start_time1}')

            # multithreading----------------------------------
            start_time = time.time()
            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = [
                    executor.submit(self.request_binance, selected_currency, self.row),
                    executor.submit(self.request_mexc, selected_currency, self.row),
                    executor.submit(self.request_bybit, selected_currency, self.row),
                    executor.submit(self.request_commex, selected_currency, self.row)
                ]

                concurrent.futures.wait(results)
            end_time = time.time()

            print(f'Time: {end_time - start_time}')
            self.row += 1

    def manual_update(self):
        i = 0

        # for key in currencies_list:
        #     if i < self.row:
        #         self.request_binance(key, i)
        #         self.request_commex(key, i)
        #         self.request_mexc(key, i)
        #         i += 1
        #     else:
        #         break
        #

        start = time.time()
        for key in currencies_list:
            with concurrent.futures.ThreadPoolExecutor() as executor:
                results = [
                    executor.submit(self.request_binance, key, i),
                    executor.submit(self.request_mexc, key, i),
                    executor.submit(self.request_bybit, key, i),
                    executor.submit(self.request_commex, key, i)
                ]
            concurrent.futures.wait(results)
        end = time.time()
        i += 1

        print(f'Time update: {end - start}')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyExchange()
    window.setWindowFlags(window.windowFlags() | Qt.WindowStaysOnTopHint)
    window.show()
    sys.exit(app.exec())
