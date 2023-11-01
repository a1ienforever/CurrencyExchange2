import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from currency_exchange_ui import Ui_MainWindow


class CurrencyExchange(QMainWindow):
    def __init__(self):
        super(CurrencyExchange, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CurrencyExchange()
    window.show()
    sys.exit(app.exec())
