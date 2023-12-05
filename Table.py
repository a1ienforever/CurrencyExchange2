from PySide6.QtWidgets import QMainWindow, QListWidgetItem

import table_main_window_ui


class Table(QMainWindow):
    i = 0
    def __init__(self):
        super(Table, self).__init__()
        self.ui = table_main_window_ui.Table_MainWindow()
        self.ui.setupUi(self)

        self.ui.date_search.clicked.connect(self.new_item)
#TODO: не работает(oblect has no attribute)
    def new_item(self):
        text = f'New Element {self.i}'
        new_item = self.ui.listPrice.item(self.i)
        new_item.setText(text)
        self.i += 1





