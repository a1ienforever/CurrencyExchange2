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
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

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
        self.treeWidget = QTreeWidget(self.ArticleFrame)
        self.treeWidget.headerItem().setText(0, "")
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setBackground(1, QColor(85, 255, 255));
        __qtreewidgetitem.setBackground(0, QColor(85, 255, 255));
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setStyleSheet(u"border: none;\n"
"")

        self.gridLayout_3.addWidget(self.treeWidget, 0, 0, 1, 1)


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
        self.comboBox = QComboBox(self.AsideFrame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 30))
        self.comboBox.setStyleSheet(u"border: 1px solid #ddedfa;\n"
"border-radius: 3px;\n"
"padding: 5px;\n"
"QComboBox::drop-down {\n"
"        width: 20px; /* \u0428\u0438\u0440\u0438\u043d\u0430 \u0441\u0442\u0440\u0435\u043b\u043a\u0438 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 */\n"
"    }")

        self.verticalLayout.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.AsideFrame)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 30))
        self.comboBox_2.setStyleSheet(u"border: 1px solid #ddedfa;\n"
"border-radius: 3px;\n"
"padding: 5px;\n"
"")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(114, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.AsideFrame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(40, 25))
        self.pushButton.setMaximumSize(QSize(70, 40))
        self.pushButton.setLayoutDirection(Qt.RightToLeft)
        self.pushButton.setStyleSheet(u"\n"
"border: 1px solid #ddedfa;\n"
"border-radius: 3px;\n"
"padding: 5px;")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.radioButton = QRadioButton(self.AsideFrame)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setMinimumSize(QSize(0, 40))
        self.radioButton.setStyleSheet(u"border: none;")

        self.verticalLayout.addWidget(self.radioButton)

        self.pushButton_2 = QPushButton(self.AsideFrame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 30))
        self.pushButton_2.setStyleSheet(u"border: 1px solid #ddedfa;\n"
"border-radius: 3px;\n"
"padding: 5px;\n"
"QPushButton::hover{\n"
"	backgound: white;\n"
"	color: black;\n"
"	font: bold;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_2)


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
        self.label = QLabel(self.HeaderFrame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.label.setStyleSheet(u"color: #ddedfa;\n"
"font: 36px;\n"
"border: none;\n"
"")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.HeaderFrame, 0, 0, 1, 2)


        self.gridLayout.addWidget(self.MainFrame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MCE", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("MainWindow", u"Price 3", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("MainWindow", u"Price 2", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"Price 1", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"Currency", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("MainWindow", u"Currency Pair", None));
        ___qtreewidgetitem2 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("MainWindow", u"Currency Pair", None));
        ___qtreewidgetitem3 = self.treeWidget.topLevelItem(2)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("MainWindow", u"Currency Pair", None));
        ___qtreewidgetitem4 = self.treeWidget.topLevelItem(3)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("MainWindow", u"Currency Pair", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Exchange 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Exchange 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Exchange 3", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Exchange", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Currency 1", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Currency 2", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Currency 3", None))

        self.comboBox_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Choose Currency", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"AutoUpdate", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Update", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Multi Currency Exchanger", None))
    # retranslateUi

