# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table_main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.delete_button = QPushButton(self.frame)
        self.delete_button.setObjectName(u"delete_item")
        self.delete_button.setMinimumSize(QSize(0, 30))
        self.delete_button.setMaximumSize(QSize(400, 100))
        self.delete_button.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.delete_button)

        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.listWidget = QListWidget(self.frame)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"border: none;\n"
                                      u"font: 24px")

        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"List of Exchange", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow",
                                                            u"Удалить запись",
                                                              None))
    # retranslateUi
