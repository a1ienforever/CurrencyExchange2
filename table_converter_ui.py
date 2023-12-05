# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table_converter.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
                               QMainWindow, QSizePolicy, QWidget)


class TableWindow(object):


    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(430, 234)
        MainWindow.setStyleSheet(u"background: #233340;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background: #233340;\n"
                                 "color: white;\n"
                                 "font-family: Ubuntu;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background: #6bd6ce;\n"
                                 "border: 2px solid #ddedfa;\n"
                                 "border-radius: 3px;\n"
                                 "font: bold;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background: #6bd6ce;\n"
                                   "border: 2px solid #ddedfa;\n"
                                   "border-radius: 3px;\n"
                                   "font: bold;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background: #6bd6ce;\n"
                                   "border: 2px solid #ddedfa;\n"
                                   "border-radius: 3px;\n"
                                   "font: bold;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setStyleSheet(u"background: #6bd6ce;\n"
                                   "border: 2px solid #ddedfa;\n"
                                   "border-radius: 3px;\n"
                                   "font: bold;")
        self.label_4.setTextFormat(Qt.AutoText)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 3, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"background: #6bd6ce;\n"
                                   "border: 2px solid #ddedfa;\n"
                                   "border-radius: 3px;\n"
                                   "font: bold;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"background: #6bd6ce;\n"
                                   "border: 2px solid #ddedfa;\n"
                                   "border-radius: 3px;\n"
                                   "font: bold;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"background: #6bd6ce;\n"
                                   "border: 2px solid #ddedfa;\n"
                                   "border-radius: 3px;\n"
                                   "font: bold;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 1, 2, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"background: #6bd6ce;\n"
                                   "border: 2px solid #ddedfa;\n"
                                   "border-radius: 3px;\n"
                                   "font: bold;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_9, 1, 3, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"background: #6bd6ce;\n"
                                   "border: 2px solid #ddedfa;\n"
                                   "border-radius: 3px;\n"
                                   "font: bold;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"background: #6bd6ce;\n"
                                    "border: 2px solid #ddedfa;\n"
                                    "border-radius: 3px;\n"
                                    "font: bold;")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_11, 2, 1, 1, 1)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"background: #6bd6ce;\n"
                                    "border: 2px solid #ddedfa;\n"
                                    "border-radius: 3px;\n"
                                    "font: bold;QLabel{\n"
                                    "text-align: center;\n"
                                    "}")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 2, 2, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"background: #6bd6ce;\n"
                                    "border: 2px solid #ddedfa;\n"
                                    "border-radius: 3px;\n"
                                    "font: bold;")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_12, 2, 3, 1, 1)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"background: #6bd6ce;\n"
                                    "border: 2px solid #ddedfa;\n"
                                    "border-radius: 3px;\n"
                                    "font: bold;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_13, 3, 0, 1, 1)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"background: #6bd6ce;\n"
                                    "border: 2px solid #ddedfa;\n"
                                    "border-radius: 3px;\n"
                                    "font: bold;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 3, 1, 1, 1)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setStyleSheet(u"background: #6bd6ce;\n"
                                    "border: 2px solid #ddedfa;\n"
                                    "border-radius: 3px;\n"
                                    "font: bold;")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_15, 3, 2, 1, 1)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setStyleSheet(u"background: #6bd6ce;\n"
                                    "border: 2px solid #ddedfa;\n"
                                    "border-radius: 3px;\n"
                                    "font: bold;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_16, 3, 3, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"RUB", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"USD", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Crypt", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.label_5.setText("")
        self.label_7.setText("")
        self.label_9.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_11.setText("")
        self.label_10.setText("")
        self.label_12.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_16.setText("")
    # retranslateUi
