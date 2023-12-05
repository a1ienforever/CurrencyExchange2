from PySide6.QtWidgets import QMainWindow
import table_converter_ui

class Table(QMainWindow):
    def __init__(self):
        super(Table, self).__init__()
        self.ui = table_converter_ui.TableWindow()
        self.ui.setupUi(self)

