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
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QTimeEdit, QVBoxLayout, QWidget)

class Ui_Trains(object):
    def setupUi(self, Trains):
        if not Trains.objectName():
            Trains.setObjectName(u"Trains")
        Trains.resize(880, 617)
        self.centralwidget = QWidget(Trains)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.widget = QWidget(self.page)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 831, 531))
        self.verticalLayout_7 = QVBoxLayout(self.widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Home = QPushButton(self.widget)
        self.Home.setObjectName(u"Home")

        self.horizontalLayout_3.addWidget(self.Home)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.Carriages = QListWidget(self.widget)
        self.Carriages.setObjectName(u"Carriages")
        self.Carriages.setFlow(QListView.Flow.LeftToRight)

        self.verticalLayout_7.addWidget(self.Carriages)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.SeatsLook = QTableWidget(self.widget)
        self.SeatsLook.setObjectName(u"SeatsLook")

        self.horizontalLayout_4.addWidget(self.SeatsLook)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.summary = QLabel(self.widget)
        self.summary.setObjectName(u"summary")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.summary.sizePolicy().hasHeightForWidth())
        self.summary.setSizePolicy(sizePolicy)
        self.summary.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.summary)

        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 404, 98))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.Booker = QPushButton(self.widget)
        self.Booker.setObjectName(u"Booker")

        self.verticalLayout_6.addWidget(self.Booker)


        self.horizontalLayout_4.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.stackedWidget.addWidget(self.page)
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Departure.sizePolicy().hasHeightForWidth())
        self.Departure.setSizePolicy(sizePolicy1)
        self.Departure.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.Departure)

        self.Arrival = QLineEdit(self.page_5)
        self.Arrival.setObjectName(u"Arrival")
        sizePolicy1.setHeightForWidth(self.Arrival.sizePolicy().hasHeightForWidth())
        self.Arrival.setSizePolicy(sizePolicy1)
        self.Arrival.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.Arrival)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.info = QLabel(self.page_5)
        self.info.setObjectName(u"info")
        sizePolicy.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.info)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(70)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dateEdit = QDateEdit(self.page_5)
        self.dateEdit.setObjectName(u"dateEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy2)
        self.dateEdit.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.dateEdit)

        self.timeEdit = QTimeEdit(self.page_5)
        self.timeEdit.setObjectName(u"timeEdit")
        sizePolicy2.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy2)
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
        self.listWidget = QListWidget(self.page_6)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 10, 771, 521))
        self.stackedWidget.addWidget(self.page_6)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        Trains.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Trains)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 880, 23))
        Trains.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Trains)
        self.statusbar.setObjectName(u"statusbar")
        Trains.setStatusBar(self.statusbar)

        self.retranslateUi(Trains)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Trains)
    # setupUi

    def retranslateUi(self, Trains):
        Trains.setWindowTitle(QCoreApplication.translate("Trains", u"Trains", None))
        self.Home.setText(QCoreApplication.translate("Trains", u"Home", None))
        self.label.setText(QCoreApplication.translate("Trains", u"Book", None))
        self.summary.setText(QCoreApplication.translate("Trains", u"Choose your Seat my Friend", None))
        self.Booker.setText(QCoreApplication.translate("Trains", u"Book", None))
        self.Departure.setInputMask("")
        self.Departure.setText("")
        self.Departure.setPlaceholderText(QCoreApplication.translate("Trains", u"Departure", None))
        self.Arrival.setInputMask("")
        self.Arrival.setText("")
        self.Arrival.setPlaceholderText(QCoreApplication.translate("Trains", u"Arrival", None))
        self.info.setText("")
        self.checkBox.setText(QCoreApplication.translate("Trains", u"Direct", None))
        self.Search.setText(QCoreApplication.translate("Trains", u"Search", None))
    # retranslateUi

