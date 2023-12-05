# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'converter.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QIntValidator)
from PySide6.QtWidgets import (QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(483, 282)
        MainWindow.setMinimumSize(QSize(483, 282))
        MainWindow.setMaximumSize(QSize(483, 282))
        MainWindow.setStyleSheet(u"background: #233340;\n"
                                 "color: #ddedfa;\n"
                                 "font-family: Ubuntu;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setAcceptDrops(True)
        self.frame.setStyleSheet(u"border: 2px solid #ddedfa;\n"
                                 "color: #ffffff;\n"
                                 "font-size: 14px solid #ccc;")
        self.frame.setInputMethodHints(Qt.ImhNoAutoUppercase)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.header = QLabel(self.frame)
        self.header.setObjectName(u"header")
        self.header.setLayoutDirection(Qt.LeftToRight)
        self.header.setStyleSheet(u"font: 24px;\n"
                                  "text-align: center")

        self.gridLayout_2.addWidget(self.header, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border: none;")

        self.horizontalLayout.addWidget(self.label_2)

        self.input_rub = QLineEdit(self.frame)
        self.validator = QIntValidator()
        self.input_rub.setValidator(self.validator)
        self.input_rub.setObjectName(u"input_rub")
        self.input_rub.setInputMethodHints(Qt.ImhDigitsOnly)

        self.horizontalLayout.addWidget(self.input_rub)

        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border: none;")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.choose_crypt = QComboBox(self.frame)
        self.choose_crypt.setObjectName(u"choose_crypt")
        self.choose_crypt.setPlaceholderText('Choose crypt')
        self.choose_crypt.addItem("BTCUSDT")
        self.choose_crypt.addItem("LTCUSDT")
        self.choose_crypt.addItem("ETHUSDT")

        self.horizontalLayout_2.addWidget(self.choose_crypt)

        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setStyleSheet(u"border: none;")

        self.horizontalLayout_4.addWidget(self.label_5)

        self.choose_exchange = QComboBox(self.frame)
        self.choose_exchange.setObjectName(u"choose_exchange")
        self.choose_exchange.setPlaceholderText('Choose Exchange')
        self.choose_exchange.addItem("Binance")
        self.choose_exchange.addItem("CommEX")
        self.choose_exchange.addItem("MEXC")

        self.horizontalLayout_4.addWidget(self.choose_exchange)

        self.gridLayout_2.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.convert_button = QPushButton(self.frame)
        self.convert_button.setObjectName(u"convert_button")
        self.convert_button.setStyleSheet(u"QPushButton{\n"
                                          "border: 1px solid #ddedfa;\n"
                                          "padding: 5px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover{\n"
                                          "background: #6bd6ce;\n"
                                          "color: black;\n"
                                          "\n"
                                          "}")

        self.horizontalLayout_3.addWidget(self.convert_button)

        self.output_result = QLineEdit(self.frame)
        self.output_result.setObjectName(u"output_result")
        self.output_result.setAcceptDrops(False)
        self.output_result.setInputMethodHints(Qt.ImhDigitsOnly)
        self.output_result.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.output_result)

        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.footer = QLabel(self.frame)
        self.footer.setObjectName(u"footer")
        self.footer.setEnabled(True)
        self.footer.setStyleSheet(u"border: none;")

        self.gridLayout_2.addWidget(self.footer, 5, 0, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.header.setText(QCoreApplication.translate("MainWindow", u"Converter", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0441\u0443\u043c\u043c\u0443 \u0432 \u0440\u0443\u0431\u043b\u044f\u0445:",
                                                        None))

        self.input_rub.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043a\u0440\u0438\u043f\u0442\u043e\u0432\u0430\u043b\u044e\u0442\u0443:",
                                                        None))
        self.label_5.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0431\u0438\u0440\u0436\u0443:",
                                                        None))
        self.convert_button.setText(QCoreApplication.translate("MainWindow", u"Convert", None))

        self.footer.setText(u'Перевод осуществлен с условием выгодного обмена доллара \n'
                            u'через банк')
