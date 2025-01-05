# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Trains'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDateEdit, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QScrollArea, QSizePolicy, QSlider,
    QSpacerItem, QStackedWidget, QStatusBar, QTableWidget,
    QTableWidgetItem, QTimeEdit, QVBoxLayout, QWidget)

class Ui_Trains(object):
    def setupUi(self, Trains):
        if not Trains.objectName():
            Trains.setObjectName(u"Trains")
        Trains.resize(1155, 842)
        self.centralwidget = QWidget(Trains)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Home = QPushButton(self.centralwidget)
        self.Home.setObjectName(u"Home")

        self.horizontalLayout_6.addWidget(self.Home)

        self.Tickets = QPushButton(self.centralwidget)
        self.Tickets.setObjectName(u"Tickets")

        self.horizontalLayout_6.addWidget(self.Tickets)

        self.IDshow = QLabel(self.centralwidget)
        self.IDshow.setObjectName(u"IDshow")
        self.IDshow.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.IDshow)

        self.Logger = QLineEdit(self.centralwidget)
        self.Logger.setObjectName(u"Logger")

        self.horizontalLayout_6.addWidget(self.Logger)

        self.Enter = QPushButton(self.centralwidget)
        self.Enter.setObjectName(u"Enter")

        self.horizontalLayout_6.addWidget(self.Enter)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")

        self.verticalLayout_7.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Carriages = QListWidget(self.page)
        self.Carriages.setObjectName(u"Carriages")
        self.Carriages.setFlow(QListView.Flow.LeftToRight)

        self.horizontalLayout_3.addWidget(self.Carriages)

        self.labelplot = QLabel(self.page)
        self.labelplot.setObjectName(u"labelplot")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelplot.sizePolicy().hasHeightForWidth())
        self.labelplot.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.labelplot)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.SeatsLook = QTableWidget(self.page)
        self.SeatsLook.setObjectName(u"SeatsLook")

        self.horizontalLayout_4.addWidget(self.SeatsLook)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.summary = QLabel(self.page)
        self.summary.setObjectName(u"summary")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.summary.sizePolicy().hasHeightForWidth())
        self.summary.setSizePolicy(sizePolicy1)
        self.summary.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.summary)

        self.scrollArea = QScrollArea(self.page)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 549, 150))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.Booker = QPushButton(self.page)
        self.Booker.setObjectName(u"Booker")

        self.verticalLayout_6.addWidget(self.Booker)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_9.addWidget(self.label_3)

        self.ListTicket = QListWidget(self.page_2)
        self.ListTicket.setObjectName(u"ListTicket")

        self.verticalLayout_9.addWidget(self.ListTicket)

        self.stackedWidget.addWidget(self.page_2)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_2 = QVBoxLayout(self.page_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(60)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(100)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.Departure = QLineEdit(self.page_5)
        self.Departure.setObjectName(u"Departure")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Departure.sizePolicy().hasHeightForWidth())
        self.Departure.setSizePolicy(sizePolicy2)
        self.Departure.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.Departure)

        self.Arrival = QLineEdit(self.page_5)
        self.Arrival.setObjectName(u"Arrival")
        sizePolicy2.setHeightForWidth(self.Arrival.sizePolicy().hasHeightForWidth())
        self.Arrival.setSizePolicy(sizePolicy2)
        self.Arrival.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.Arrival)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.info = QLabel(self.page_5)
        self.info.setObjectName(u"info")
        sizePolicy1.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.info)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(70)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dateEdit = QDateEdit(self.page_5)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy3)
        self.dateEdit.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.dateEdit)

        self.timeEdit = QTimeEdit(self.page_5)
        self.timeEdit.setObjectName(u"timeEdit")
        sizePolicy3.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy3)
        self.timeEdit.setCalendarPopup(False)

        self.horizontalLayout_2.addWidget(self.timeEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 229, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.checkBox = QCheckBox(self.page_5)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setIconSize(QSize(32, 32))
        self.checkBox.setChecked(True)

        self.verticalLayout_4.addWidget(self.checkBox)

        self.Search = QPushButton(self.page_5)
        self.Search.setObjectName(u"Search")

        self.verticalLayout_4.addWidget(self.Search)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_10 = QVBoxLayout(self.page_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.listWidget = QListWidget(self.page_6)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_10.addWidget(self.listWidget)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Compartemnts = QCheckBox(self.page_6)
        self.Compartemnts.setObjectName(u"Compartemnts")

        self.horizontalLayout_8.addWidget(self.Compartemnts)

        self.Compartemnts1 = QCheckBox(self.page_6)
        self.Compartemnts1.setObjectName(u"Compartemnts1")

        self.horizontalLayout_8.addWidget(self.Compartemnts1)


        self.verticalLayout_10.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.Table = QCheckBox(self.page_6)
        self.Table.setObjectName(u"Table")

        self.horizontalLayout_9.addWidget(self.Table)

        self.Table1 = QCheckBox(self.page_6)
        self.Table1.setObjectName(u"Table1")

        self.horizontalLayout_9.addWidget(self.Table1)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.corridor_middle_window = QCheckBox(self.page_6)
        self.corridor_middle_window.setObjectName(u"corridor_middle_window")

        self.horizontalLayout_10.addWidget(self.corridor_middle_window)

        self.CMW1 = QSlider(self.page_6)
        self.CMW1.setObjectName(u"CMW1")
        self.CMW1.setMaximum(2)
        self.CMW1.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_10.addWidget(self.CMW1)


        self.verticalLayout_10.addLayout(self.horizontalLayout_10)

        self.label_2 = QLabel(self.page_6)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_10.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page_6)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        Trains.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Trains)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1155, 23))
        Trains.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Trains)
        self.statusbar.setObjectName(u"statusbar")
        Trains.setStatusBar(self.statusbar)

        self.retranslateUi(Trains)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Trains)
    # setupUi

    def retranslateUi(self, Trains):
        Trains.setWindowTitle(QCoreApplication.translate("Trains", u"Trains", None))
        self.Home.setText(QCoreApplication.translate("Trains", u"Home", None))
        self.Tickets.setText(QCoreApplication.translate("Trains", u"Your Tickets", None))
        self.IDshow.setText(QCoreApplication.translate("Trains", u"Your ID", None))
        self.Logger.setInputMask("")
        self.Logger.setPlaceholderText(QCoreApplication.translate("Trains", u"input your ID / if not it will create new accont", None))
        self.Enter.setText(QCoreApplication.translate("Trains", u"Enter", None))
        self.label.setText(QCoreApplication.translate("Trains", u"Book", None))
        self.labelplot.setText(QCoreApplication.translate("Trains", u"TextLabel", None))
        self.summary.setText(QCoreApplication.translate("Trains", u"Choose your Seat my Friend", None))
        self.Booker.setText(QCoreApplication.translate("Trains", u"Book", None))
        self.label_3.setText(QCoreApplication.translate("Trains", u"Your Tickets", None))
        self.Departure.setInputMask("")
        self.Departure.setText("")
        self.Departure.setPlaceholderText(QCoreApplication.translate("Trains", u"Departure", None))
        self.Arrival.setInputMask("")
        self.Arrival.setText("")
        self.Arrival.setPlaceholderText(QCoreApplication.translate("Trains", u"Arrival", None))
        self.info.setText("")
        self.checkBox.setText(QCoreApplication.translate("Trains", u"Direct", None))
        self.Search.setText(QCoreApplication.translate("Trains", u"Search", None))
        self.Compartemnts.setText(QCoreApplication.translate("Trains", u"Compartemnts", None))
        self.Compartemnts1.setText(QCoreApplication.translate("Trains", u"Compartments", None))
        self.Table.setText(QCoreApplication.translate("Trains", u"Table", None))
        self.Table1.setText(QCoreApplication.translate("Trains", u"Table", None))
        self.corridor_middle_window.setText(QCoreApplication.translate("Trains", u"window_middle_corridor", None))
        self.label_2.setText(QCoreApplication.translate("Trains", u"Check if you want to include in the filter.", None))
    # retranslateUi

