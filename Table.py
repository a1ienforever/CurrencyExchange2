import datetime


from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QTreeWidget, QTreeWidgetItem

import table_main_window_ui


class Table(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = table_main_window_ui.Table_MainWindow()
        self.ui.setupUi(self)
        self.ui.delete_button.clicked.connect(self.delete)

    def add_item(self, text):
        item = QListWidgetItem(text)
        self.ui.listWidget.addItem(item)

    def update_list(self):
        import sqlite3
        with sqlite3.connect('database.sqlite') as db:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM conversion')
            items = cursor.fetchall()
            for item in items:
                string = f"{item[0]} {item[1]} rub -> {item[2]} usd -> {float(item[3]):.5f}{item[4]}"
                self.ui.listWidget.addItem(str(string))

    def delete(self):
        self.delete_from_db()
        self.delete_item()

    def delete_item(self):
        selected_items = self.ui.listWidget.selectedItems()
        if len(selected_items) > 0:
            selected_item = selected_items[0]
            row = self.ui.listWidget.row(selected_item)
            self.ui.listWidget.takeItem(row)
            self.ui.listWidget.repaint()

    def delete_from_db(self):
        item = self.ui.listWidget.currentItem().text()
        date = item[0:16]
        if item:
            import sqlite3
            with sqlite3.connect('database.sqlite') as db:
                cursor = db.cursor()
                cursor.execute('DELETE FROM conversion WHERE datetime = ?',(date,))
                print('Запись удалена!')



