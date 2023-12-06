import datetime

from PySide6.QtWidgets import QMainWindow, QListWidgetItem

import table_main_window_ui
from Converter import Converter


class Table(QMainWindow):
    i = 0

    def __init__(self):
        self.converter = Converter()
        super(Table, self).__init__()
        self.ui = table_main_window_ui.Table_MainWindow()
        self.ui.setupUi(self)
        self.ui.date_search.clicked.connect(self.new_item)

    def new_item(self):
        text = f'New Element {self.i}'
        self.ui.listPrice.addItem(text)
        self.i += 1

        self.converter.get_result()

    def get_datetime(self):
        current_datetime = datetime.datetime.now()
        formatted_datetime = current_datetime.strftime("%d.%m.%Y %H:%M")
        return formatted_datetime


