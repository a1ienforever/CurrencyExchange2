import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from currency_exchange_ui import Ui_MainWindow
import requests
import data



class CurrencyExchange(QMainWindow):
    def __init__(self):
        super(CurrencyExchange, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.manual_update.clicked.connect(self.parser)
        self.ui.pushButton.clicked.connect(self.add_currency_pair)

    def parser(self):
        # Перенести все в массив
        data_binance = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT').json()
        data_commex = requests.get('https://api.commex.com/api/v1/ticker/price?symbol=BTCUSDT').json()
        price_commex = f"{float(data_commex['price']):.3f}"
        currency_commex = str(data_commex['symbol'])
        price_binance = f"{float(data_binance['price']):.3f}"
        currency_binance = str(data_binance['symbol'])
        name_exchange = 'Binance'
        self.ui.tableWidget.horizontalHeaderItem(0).setText(name_exchange)
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(price_binance))
        self.ui.tableWidget.verticalHeaderItem(0).setText(currency_binance)

        self.ui.tableWidget.horizontalHeaderItem(1).setText('CommEX')
        self.ui.tableWidget.setItem(0, 1, QTableWidgetItem(price_commex))


    def add_currency_pair(self):
        selected_currency = self.ui.box_currency.currentText()
        selected_exchanger = self.ui.box_exchange.currentText()
        print(selected_exchanger)
        print(selected_currency)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyExchange()
    window.show()
    sys.exit(app.exec())



