import datetime

from PySide6.QtWidgets import QMainWindow, QListWidgetItem

import table_main_window_ui


class Table(QMainWindow):

    def __init__(self):
        super(Table, self).__init__()
        self.ui = table_main_window_ui.Table_MainWindow()
        self.ui.setupUi(self)
        # self.ui.date_search.clicked.connect(self.new_item)

    def new_item(self, text):
        self.ui.listPrice.addItem('Hello World')
