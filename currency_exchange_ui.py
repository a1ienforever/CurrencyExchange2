# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'currency_exchange_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QHeaderView, QLabel, QMainWindow,
                               QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
                               QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(818, 468)
        MainWindow.setMinimumSize(QSize(818, 468))
        MainWindow.setMaximumSize(QSize(818, 468))
        MainWindow.setStyleSheet(u"background: #233340;\n"
                                 "color: #ddedfa;\n"
                                 "font-family: Ubuntu;")
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.MainFrame = QFrame(self.centralwidget)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setMinimumSize(QSize(800, 450))
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.MainFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ArticleFrame = QFrame(self.MainFrame)
        self.ArticleFrame.setObjectName(u"ArticleFrame")
        self.ArticleFrame.setMinimumSize(QSize(550, 0))
        self.ArticleFrame.setStyleSheet(u"border: 2px solid #ddedfa;\n"
                                        "border-radius: 10px;\n"
                                        "QTreeView {\n"
                                        "    background-color: #0078d4; /* \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 */\n"
                                        "    color: #ffffff; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 */\n"
                                        "    border: 1px solid #ccc; /* \u0420\u0430\u043c\u043a\u0430 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 */\n"
                                        "    font-size: 14px; /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0430 */\n"
                                        "}")
        self.ArticleFrame.setFrameShape(QFrame.StyledPanel)
        self.ArticleFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.ArticleFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget = QTableWidget(self.ArticleFrame)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(False)
        self.tableWidget.setMinimumSize(QSize(200, 300))
        self.tableWidget.setStyleSheet(u"border: none;\n"
                                       "background-color: none;\n"
                                       "color: black;\n"
                                       "")

        self.gridLayout_3.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.horizontalLayout_2.addWidget(self.ArticleFrame)

        self.AsideFrame = QFrame(self.MainFrame)
        self.AsideFrame.setObjectName(u"AsideFrame")
        self.AsideFrame.setMinimumSize(QSize(200, 0))
        self.AsideFrame.setStyleSheet(u"border: 2px solid #ddedfa;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 5px;")
        self.AsideFrame.setFrameShape(QFrame.StyledPanel)
        self.AsideFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.AsideFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.box_exchange = QComboBox(self.AsideFrame)
        self.box_exchange.setPlaceholderText('Choose exchange')
        self.box_exchange.addItem("")
        self.box_exchange.addItem("")
        self.box_exchange.addItem("")
        self.box_exchange.setObjectName(u"box_exchange")
        self.box_exchange.setMinimumSize(QSize(0, 30))
        self.box_exchange.setStyleSheet(u"border: 1px solid #ddedfa;\n"
                                        "border-radius: 3px;\n"
                                        "padding: 5px;\n"
                                        "QComboBox::drop-down {\n"
                                        "        width: 20px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u0441\u0442\u0440\u0435\u043b\u043a\u0438 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
                                        "    }")

        self.verticalLayout.addWidget(self.box_exchange)

        self.box_currency = QComboBox(self.AsideFrame)
        self.box_currency.setPlaceholderText('Choose currency')
        self.box_currency.addItem("")
        self.box_currency.addItem("")
        self.box_currency.addItem("")
        self.box_currency.setObjectName(u"box_currency")
        self.box_currency.setMinimumSize(QSize(0, 30))
        self.box_currency.setStyleSheet(u"border: 1px solid #ddedfa;\n"
                                        "border-radius: 3px;\n"
                                        "padding: 5px;\n"
                                        "")

        self.verticalLayout.addWidget(self.box_currency)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(114, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.AsideFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(40, 25))
        self.pushButton.setMaximumSize(QSize(70, 40))
        self.pushButton.setLayoutDirection(Qt.RightToLeft)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
                                      "border: 1px solid #ddedfa;\n"
                                      "border-radius: 3px;\n"
                                      "padding: 5px;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "	background: #6bd6ce;\n"
                                      "	color: black;\n"
                                      "	font: bold;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover:pressed{\n"
                                      "	background: white;\n"
                                      "}")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.auto_update_button = QRadioButton(self.AsideFrame)
        self.auto_update_button.setObjectName(u"auto_update_button")
        self.auto_update_button.setMinimumSize(QSize(0, 40))
        self.auto_update_button.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.auto_update_button)

        self.manual_update = QPushButton(self.AsideFrame)
        self.manual_update.setObjectName(u"manual_update")
        self.manual_update.setMinimumSize(QSize(0, 30))
        self.manual_update.setStyleSheet(u"QPushButton{\n"
                                         "border: 1px solid #ddedfa;\n"
                                         "border-radius: 3px;\n"
                                         "padding: 5px;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "	background: #6bd6ce;\n"
                                         "	color: black;\n"
                                         "	font: bold;\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover:pressed{\n"
                                         "	background: white;\n"
                                         "}")

        self.verticalLayout.addWidget(self.manual_update)

        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 165, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.horizontalLayout_2.addWidget(self.AsideFrame)

        self.gridLayout_5.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.HeaderFrame = QFrame(self.MainFrame)
        self.HeaderFrame.setObjectName(u"HeaderFrame")
        self.HeaderFrame.setMinimumSize(QSize(750, 70))
        self.HeaderFrame.setMaximumSize(QSize(795, 16777215))
        self.HeaderFrame.setStyleSheet(u"font: 24px;\n"
                                       "border: 3px solid #ddedfa;\n"
                                       "border-radius: 10px;")
        self.HeaderFrame.setFrameShape(QFrame.StyledPanel)
        self.HeaderFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.HeaderFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.title_label = QLabel(self.HeaderFrame)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMinimumSize(QSize(0, 50))
        self.title_label.setStyleSheet(u"color: #ddedfa;\n"
                                       "font: 36px;\n"
                                       "border: none;\n"
                                       "")

        self.gridLayout_2.addWidget(self.title_label, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.HeaderFrame, 0, 0, 1, 2)

        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MCE", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem3 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        self.box_exchange.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Exchange", None))
        self.box_exchange.setItemText(0, QCoreApplication.translate("MainWindow", u"CommEX", None))
        self.box_exchange.setItemText(1, QCoreApplication.translate("MainWindow", u"Binance", None))
        self.box_exchange.setItemText(2, QCoreApplication.translate("MainWindow", u"TradingView", None))

        self.box_currency.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Currency", None))
        self.box_currency.setItemText(0, QCoreApplication.translate("MainWindow", u"BTC(USDT)", None))
        self.box_currency.setItemText(1, QCoreApplication.translate("MainWindow", u"ETH(USDT)", None))
        self.box_currency.setItemText(2, QCoreApplication.translate("MainWindow", u"LTC(USDT)", None))

        self.box_currency.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Currency", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.auto_update_button.setText(QCoreApplication.translate("MainWindow", u"AutoUpdate", None))
        self.manual_update.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Multi Currency Exchanger", None))
    # retranslateUi
