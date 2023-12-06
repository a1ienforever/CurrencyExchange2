# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGridLayout,
                               QHBoxLayout, QListWidget, QListWidgetItem, QMainWindow,
                               QPushButton, QSizePolicy, QWidget)


class Table_MainWindow(object):
    listPrice = None

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 400)
        MainWindow.setMinimumSize(QSize(800, 400))
        MainWindow.setMaximumSize(QSize(800, 400))
        MainWindow.setStyleSheet(u"background-color: #233340;\n"
                                 "color: #ddedfa;\n"
                                 "font-family: Ubuntu;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listPrice = QListWidget(self.frame)
        QListWidgetItem(self.listPrice)
        self.listPrice.setObjectName(u"listPrice")
        self.listPrice.setStyleSheet(u"font: 24px;\n"
                                     "border: 3px white solid")

        self.gridLayout_2.addWidget(self.listPrice, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.date_search = QPushButton(self.frame)
        self.date_search.setObjectName(u"date_search")
        self.date_search.setMinimumSize(QSize(0, 30))
        self.date_search.setMaximumSize(QSize(400, 100))
        self.date_search.setStyleSheet(u"QPushButton{\n"
                                       "border: 1px solid #ddedfa;\n"
                                       "border-radius: 3px;\n"
                                       "padding: 5px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover{\n"
                                       "background: #6bd6ce;\n"
                                       "color: black;\n"
                                       "font: bold;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover:pressed{\n"
                                       "background: white;\n"
                                       "}")

        self.horizontalLayout.addWidget(self.date_search)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.dateEdit)

        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        __sortingEnabled = self.listPrice.isSortingEnabled()
        self.listPrice.setSortingEnabled(False)
        ___qlistwidgetitem = self.listPrice.item(0)
        ___qlistwidgetitem.setText(
            QCoreApplication.translate("MainWindow", u"05/12/2023 21:45: RUB(1000) -> USD(10) -> Crypt(0.00000001)",
                                       None));
        self.listPrice.setSortingEnabled(__sortingEnabled)

        self.date_search.setText(QCoreApplication.translate("MainWindow",
                                                            u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0414\u0430\u0442\u0435",
                                                            None))
