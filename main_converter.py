import sys

from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox

from converter_ui import Ui_Converter


class Converter(QMainWindow):
    def __init__(self):
        super(Converter, self).__init__()
        self.ui = Ui_Converter()
        self.ui.setupUi(self)

    def open_converter(self):
        app2 = QApplication(sys.argv)
        window2 = Converter()
        window2.show()
        sys.exit(app2.exec())
