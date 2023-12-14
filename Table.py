import datetime

from PyQt5.QtCore import QCoreApplication
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QTreeWidget, QTreeWidgetItem

import table_main_window_ui


class Table(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = table_main_window_ui.Table_MainWindow()
        self.ui.setupUi(self)

    def add_item(self, text):
        item = QListWidgetItem(text)
        self.ui.listWidget.addItem(item)
