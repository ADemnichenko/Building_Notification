# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/building_notification_3.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(449, 551)
        MainWindow.setMinimumSize(QtCore.QSize(449, 551))
        MainWindow.setMaximumSize(QtCore.QSize(449, 551))
        MainWindow.setStyleSheet("QMainWindow {\n"
"    background-color: rgb(81, 81, 81);\n"
"}")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(411, 442))
        self.tabWidget.setMaximumSize(QtCore.QSize(411, 520))
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setStyleSheet("QTabWidget::pane { /* The tab widget frame */\n"
"    border-top: 2px solid rgb(140, 140, 140);\n"
"    position: absolute;\n"
"    top: -0.1em;\n"
"}\n"
"/* Style the tab using the tab sub-control. Note that\n"
"    it reads QTabBar _not_ QTabWidget */\n"
"QTabBar::tab {\n"
"    color: rgb(80, 80, 80);\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(155, 155, 155, 255));\n"
"    border: 1px solid rgb(140, 140, 140);\n"
"    border-top-left-radius:2px;\n"
"    border-top-right-radius: 2px;\n"
"    min-width: 8ex;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #9B9B9B;\n"
"}\n"
"")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.stngs = QtWidgets.QWidget()
        self.stngs.setObjectName("stngs")
        self.frame_5 = QtWidgets.QFrame(self.stngs)
        self.frame_5.setGeometry(QtCore.QRect(0, 10, 409, 481))
        self.frame_5.setMinimumSize(QtCore.QSize(409, 481))
        self.frame_5.setMaximumSize(QtCore.QSize(409, 481))
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox = QtWidgets.QGroupBox(self.frame_5)
        self.groupBox.setMaximumSize(QtCore.QSize(391, 90))
        self.groupBox.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setMinimumSize(QtCore.QSize(365, 57))
        self.frame.setMaximumSize(QtCore.QSize(365, 57))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fld_proj_path = QtWidgets.QLineEdit(self.frame)
        self.fld_proj_path.setMinimumSize(QtCore.QSize(306, 31))
        self.fld_proj_path.setMaximumSize(QtCore.QSize(306, 31))
        self.fld_proj_path.setStyleSheet("QLineEdit{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.fld_proj_path.setText("")
        self.fld_proj_path.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_proj_path.setObjectName("fld_proj_path")
        self.gridLayout_2.addWidget(self.fld_proj_path, 0, 0, 1, 1)
        self.btn_proj_dir = QtWidgets.QToolButton(self.frame)
        self.btn_proj_dir.setMinimumSize(QtCore.QSize(41, 31))
        self.btn_proj_dir.setStyleSheet("QToolButton { /* all types of tool button */\n"
"     border-left:1px solid rgb(75, 75, 75);\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(155, 155, 155, 255));\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}")
        self.btn_proj_dir.setObjectName("btn_proj_dir")
        self.gridLayout_2.addWidget(self.btn_proj_dir, 0, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_5)
        self.groupBox_2.setMinimumSize(QtCore.QSize(391, 150))
        self.groupBox_2.setMaximumSize(QtCore.QSize(391, 150))
        self.groupBox_2.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.frame_3 = QtWidgets.QFrame(self.groupBox_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_6.setContentsMargins(20, -1, 5, 0)
        self.gridLayout_6.setHorizontalSpacing(0)
        self.gridLayout_6.setVerticalSpacing(10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setMinimumSize(QtCore.QSize(46, 13))
        self.label.setMaximumSize(QtCore.QSize(46, 13))
        self.label.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem, 0, 1, 1, 1)
        self.fld_email = QtWidgets.QLineEdit(self.frame_3)
        self.fld_email.setMinimumSize(QtCore.QSize(241, 31))
        self.fld_email.setMaximumSize(QtCore.QSize(241, 31))
        self.fld_email.setStyleSheet("QLineEdit{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.fld_email.setText("")
        self.fld_email.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_email.setObjectName("fld_email")
        self.gridLayout_6.addWidget(self.fld_email, 0, 2, 1, 1)
        self.fld_password = QtWidgets.QLineEdit(self.frame_3)
        self.fld_password.setMinimumSize(QtCore.QSize(241, 31))
        self.fld_password.setMaximumSize(QtCore.QSize(241, 31))
        self.fld_password.setStyleSheet("QLineEdit{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.fld_password.setText("")
        self.fld_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.fld_password.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_password.setObjectName("fld_password")
        self.gridLayout_6.addWidget(self.fld_password, 1, 2, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(191, 8, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem1, 0, 0, 1, 1)
        self.btn_connection = QtWidgets.QPushButton(self.frame_4)
        self.btn_connection.setMinimumSize(QtCore.QSize(121, 21))
        self.btn_connection.setMaximumSize(QtCore.QSize(121, 21))
        self.btn_connection.setStyleSheet("QPushButton { /* all types of tool button */\n"
"    color: rgb(80, 80, 80);\n"
"     border-left:1px solid rgb(75, 75, 75);\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(155, 155, 155, 255));\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}")
        self.btn_connection.setObjectName("btn_connection")
        self.gridLayout_7.addWidget(self.btn_connection, 0, 1, 1, 1)
        self.gridLayout_6.addWidget(self.frame_4, 2, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setMinimumSize(QtCore.QSize(46, 13))
        self.label_2.setStyleSheet("QLabel{    \n"
"color: rgb(203, 203, 203);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 1, 0, 1, 2)
        self.gridLayout_8.addWidget(self.frame_3, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_2, 4, 0, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_5)
        self.groupBox_4.setMinimumSize(QtCore.QSize(391, 88))
        self.groupBox_4.setMaximumSize(QtCore.QSize(391, 88))
        self.groupBox_4.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.frame_6 = QtWidgets.QFrame(self.groupBox_4)
        self.frame_6.setMinimumSize(QtCore.QSize(365, 55))
        self.frame_6.setMaximumSize(QtCore.QSize(365, 55))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.fld_ipa_or_pak_dir = QtWidgets.QLineEdit(self.frame_6)
        self.fld_ipa_or_pak_dir.setMinimumSize(QtCore.QSize(306, 31))
        self.fld_ipa_or_pak_dir.setMaximumSize(QtCore.QSize(306, 31))
        self.fld_ipa_or_pak_dir.setStyleSheet("QLineEdit{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.fld_ipa_or_pak_dir.setText("")
        self.fld_ipa_or_pak_dir.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_ipa_or_pak_dir.setReadOnly(False)
        self.fld_ipa_or_pak_dir.setObjectName("fld_ipa_or_pak_dir")
        self.gridLayout_10.addWidget(self.fld_ipa_or_pak_dir, 0, 0, 1, 1)
        self.btn_ipa_or_pak_dir = QtWidgets.QToolButton(self.frame_6)
        self.btn_ipa_or_pak_dir.setMinimumSize(QtCore.QSize(41, 31))
        self.btn_ipa_or_pak_dir.setMaximumSize(QtCore.QSize(41, 31))
        self.btn_ipa_or_pak_dir.setStyleSheet("QToolButton { /* all types of tool button */\n"
"     border-left:1px solid rgb(75, 75, 75);\n"
"    border-top-right-radius: 8px;\n"
"    border-bottom-right-radius: 8px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(155, 155, 155, 255));\n"
"}\n"
"QToolButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}\n"
"QToolButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}")
        self.btn_ipa_or_pak_dir.setObjectName("btn_ipa_or_pak_dir")
        self.gridLayout_10.addWidget(self.btn_ipa_or_pak_dir, 0, 1, 1, 1)
        self.gridLayout_11.addWidget(self.frame_6, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_4, 3, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_5)
        self.groupBox_3.setMinimumSize(QtCore.QSize(391, 90))
        self.groupBox_3.setMaximumSize(QtCore.QSize(391, 90))
        self.groupBox_3.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.groupBox_3)
        self.frame_2.setMinimumSize(QtCore.QSize(365, 57))
        self.frame_2.setMaximumSize(QtCore.QSize(365, 57))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.fld_proj_name = QtWidgets.QLineEdit(self.frame_2)
        self.fld_proj_name.setMinimumSize(QtCore.QSize(340, 31))
        self.fld_proj_name.setMaximumSize(QtCore.QSize(340, 31))
        self.fld_proj_name.setStyleSheet("QLineEdit{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.fld_proj_name.setText("")
        self.fld_proj_name.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_proj_name.setObjectName("fld_proj_name")
        self.gridLayout_4.addWidget(self.fld_proj_name, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.frame_2, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.stngs, "")
        self.ntfctn = QtWidgets.QWidget()
        self.ntfctn.setStyleSheet("")
        self.ntfctn.setObjectName("ntfctn")
        self.frame_8 = QtWidgets.QFrame(self.ntfctn)
        self.frame_8.setGeometry(QtCore.QRect(0, 10, 415, 481))
        self.frame_8.setMinimumSize(QtCore.QSize(415, 481))
        self.frame_8.setMaximumSize(QtCore.QSize(415, 481))
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setSpacing(0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_8)
        self.groupBox_5.setMinimumSize(QtCore.QSize(391, 63))
        self.groupBox_5.setMaximumSize(QtCore.QSize(391, 63))
        self.groupBox_5.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox_5)
        self.timeEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeEdit.sizePolicy().hasHeightForWidth())
        self.timeEdit.setSizePolicy(sizePolicy)
        self.timeEdit.setMinimumSize(QtCore.QSize(140, 30))
        self.timeEdit.setMaximumSize(QtCore.QSize(140, 30))
        self.timeEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.timeEdit.setStyleSheet("#timeEdit{\n"
"    color: rgb(203, 203, 203);\n"
"    font: italic 25pt \"Helvetica Neue\";\n"
"    background-color: rgba(253, 96, 118, 0);\n"
"}\n"
"")
        self.timeEdit.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.timeEdit.setWrapping(True)
        self.timeEdit.setFrame(False)
        self.timeEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.timeEdit.setReadOnly(True)
        self.timeEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timeEdit.setKeyboardTracking(True)
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout_12.addWidget(self.timeEdit, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem2, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem3, 0, 2, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_5, 1, 0, 1, 1)
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame_8)
        self.groupBox_6.setMinimumSize(QtCore.QSize(391, 210))
        self.groupBox_6.setMaximumSize(QtCore.QSize(391, 210))
        self.groupBox_6.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.frame_7 = QtWidgets.QFrame(self.groupBox_6)
        self.frame_7.setMinimumSize(QtCore.QSize(371, 190))
        self.frame_7.setMaximumSize(QtCore.QSize(371, 190))
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.chb_parse_log = QtWidgets.QCheckBox(self.frame_7)
        self.chb_parse_log.setMinimumSize(QtCore.QSize(108, 31))
        self.chb_parse_log.setMaximumSize(QtCore.QSize(108, 31))
        self.chb_parse_log.setStyleSheet("QCheckBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding-left : 8px;\n"
"}")
        self.chb_parse_log.setCheckable(True)
        self.chb_parse_log.setChecked(False)
        self.chb_parse_log.setObjectName("chb_parse_log")
        self.gridLayout_13.addWidget(self.chb_parse_log, 0, 0, 1, 1)
        self.chb_extract_ipa = QtWidgets.QCheckBox(self.frame_7)
        self.chb_extract_ipa.setMinimumSize(QtCore.QSize(108, 31))
        self.chb_extract_ipa.setMaximumSize(QtCore.QSize(108, 31))
        self.chb_extract_ipa.setStyleSheet("QCheckBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding-left : 8px;\n"
"}")
        self.chb_extract_ipa.setObjectName("chb_extract_ipa")
        self.gridLayout_13.addWidget(self.chb_extract_ipa, 0, 1, 1, 1)
        self.chb_send_to_email = QtWidgets.QCheckBox(self.frame_7)
        self.chb_send_to_email.setMinimumSize(QtCore.QSize(108, 31))
        self.chb_send_to_email.setMaximumSize(QtCore.QSize(108, 31))
        self.chb_send_to_email.setStyleSheet("QCheckBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding-left : 8px;\n"
"}")
        self.chb_send_to_email.setObjectName("chb_send_to_email")
        self.gridLayout_13.addWidget(self.chb_send_to_email, 0, 2, 1, 1)
        self.chb_unpackpak = QtWidgets.QCheckBox(self.frame_7)
        self.chb_unpackpak.setMinimumSize(QtCore.QSize(108, 31))
        self.chb_unpackpak.setMaximumSize(QtCore.QSize(108, 31))
        self.chb_unpackpak.setStyleSheet("QCheckBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding-left : 8px;\n"
"}")
        self.chb_unpackpak.setObjectName("chb_unpackpak")
        self.gridLayout_13.addWidget(self.chb_unpackpak, 1, 0, 1, 1)
        self.chb_get_size = QtWidgets.QCheckBox(self.frame_7)
        self.chb_get_size.setMinimumSize(QtCore.QSize(108, 31))
        self.chb_get_size.setMaximumSize(QtCore.QSize(108, 31))
        self.chb_get_size.setStyleSheet("QCheckBox{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding-left : 8px;\n"
"}")
        self.chb_get_size.setObjectName("chb_get_size")
        self.gridLayout_13.addWidget(self.chb_get_size, 1, 1, 1, 1)
        self.frame_11 = QtWidgets.QFrame(self.frame_7)
        self.frame_11.setMinimumSize(QtCore.QSize(360, 60))
        self.frame_11.setMaximumSize(QtCore.QSize(360, 60))
        self.frame_11.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_4 = QtWidgets.QLabel(self.frame_11)
        self.label_4.setMinimumSize(QtCore.QSize(340, 15))
        self.label_4.setMaximumSize(QtCore.QSize(340, 15))
        self.label_4.setStyleSheet("QLabel{    color: rgb(203, 203, 203);}")
        self.label_4.setObjectName("label_4")
        self.gridLayout_17.addWidget(self.label_4, 0, 0, 1, 1)
        self.pb_progress = QtWidgets.QProgressBar(self.frame_11)
        self.pb_progress.setMinimumSize(QtCore.QSize(330, 15))
        self.pb_progress.setMaximumSize(QtCore.QSize(340, 15))
        self.pb_progress.setStyleSheet("QProgressBar {\n"
"    color: rgb(80, 80, 80);\n"
"    border: 1px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"    width: 10px;\n"
"}")
        self.pb_progress.setProperty("value", 50)
        self.pb_progress.setObjectName("pb_progress")
        self.gridLayout_17.addWidget(self.pb_progress, 1, 0, 1, 1)
        self.gridLayout_13.addWidget(self.frame_11, 2, 0, 1, 3)
        self.gridLayout_14.addWidget(self.frame_7, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_6, 2, 0, 1, 1)
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setMinimumSize(QtCore.QSize(397, 45))
        self.frame_10.setMaximumSize(QtCore.QSize(397, 45))
        self.frame_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_20.setSpacing(0)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.frame_9 = QtWidgets.QFrame(self.frame_10)
        self.frame_9.setMinimumSize(QtCore.QSize(180, 40))
        self.frame_9.setMaximumSize(QtCore.QSize(180, 40))
        self.frame_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.btn_cancel = QtWidgets.QPushButton(self.frame_9)
        self.btn_cancel.setMinimumSize(QtCore.QSize(75, 23))
        self.btn_cancel.setMaximumSize(QtCore.QSize(75, 23))
        self.btn_cancel.setStyleSheet("QPushButton { /* all types of tool button */\n"
"    color: rgb(80, 80, 80);\n"
"     border-left:1px solid rgb(75, 75, 75);\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(155, 155, 155, 255));\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}")
        self.btn_cancel.setObjectName("btn_cancel")
        self.gridLayout_16.addWidget(self.btn_cancel, 0, 3, 1, 1)
        self.btn_start = QtWidgets.QPushButton(self.frame_9)
        self.btn_start.setMinimumSize(QtCore.QSize(75, 23))
        self.btn_start.setMaximumSize(QtCore.QSize(75, 23))
        self.btn_start.setStyleSheet("QPushButton { /* all types of tool button */\n"
"    color: rgb(80, 80, 80);\n"
"     border-left:1px solid rgb(75, 75, 75);\n"
"    border-radius: 5px;\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(111, 111, 111, 255), stop:1 rgba(155, 155, 155, 255));\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: qlineargradient(spread:pad, x1:0.489045, y1:1, x2:0.472, y2:0, stop:0 rgba(158, 158, 158, 255), stop:1 rgba(203, 203, 203, 255));\n"
"}")
        self.btn_start.setObjectName("btn_start")
        self.gridLayout_16.addWidget(self.btn_start, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem4, 0, 2, 1, 1)
        self.gridLayout_20.addWidget(self.frame_9, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_20.addItem(spacerItem5, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.frame_10, 3, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame_8)
        self.groupBox_7.setMinimumSize(QtCore.QSize(391, 90))
        self.groupBox_7.setMaximumSize(QtCore.QSize(391, 90))
        self.groupBox_7.setStyleSheet("QGroupBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    margin-top: 1ex; /* leave space at the top for the title */\n"
"}\n"
"QGroupBox::title {\n"
"    color: rgb(203, 203, 203);\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* position at the top center */\n"
"    padding: 0 3px;\n"
"}\n"
"")
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.frame_12 = QtWidgets.QFrame(self.groupBox_7)
        self.frame_12.setMinimumSize(QtCore.QSize(365, 57))
        self.frame_12.setMaximumSize(QtCore.QSize(365, 57))
        self.frame_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.fld_rcpnts_email = QtWidgets.QLineEdit(self.frame_12)
        self.fld_rcpnts_email.setMinimumSize(QtCore.QSize(340, 31))
        self.fld_rcpnts_email.setMaximumSize(QtCore.QSize(340, 31))
        self.fld_rcpnts_email.setStyleSheet("QLineEdit{\n"
"color: rgb(203, 203, 203);\n"
"background-color: rgb(117, 117, 117);\n"
"border-radius: 8px;\n"
"padding: 5px;\n"
"}")
        self.fld_rcpnts_email.setText("")
        self.fld_rcpnts_email.setAlignment(QtCore.Qt.AlignCenter)
        self.fld_rcpnts_email.setObjectName("fld_rcpnts_email")
        self.gridLayout_19.addWidget(self.fld_rcpnts_email, 0, 0, 1, 1)
        self.gridLayout_18.addWidget(self.frame_12, 0, 0, 1, 1)
        self.gridLayout_15.addWidget(self.groupBox_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.ntfctn, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("QStatusBar{\n"
"background-color: rgb(81, 81, 81);\n"
"color: rgb(203, 203, 203);}")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Building Notification"))
        self.groupBox.setTitle(_translate("MainWindow", "Game Directory"))
        self.fld_proj_path.setPlaceholderText(_translate("MainWindow", "Select Game Directory"))
        self.btn_proj_dir.setText(_translate("MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("MainWindow", "Authorization"))
        self.label.setText(_translate("MainWindow", "Email :"))
        self.fld_email.setPlaceholderText(_translate("MainWindow", "Enter Email"))
        self.fld_password.setPlaceholderText(_translate("MainWindow", "Enter Password"))
        self.btn_connection.setText(_translate("MainWindow", "Test Connection"))
        self.label_2.setText(_translate("MainWindow", "Password :"))
        self.groupBox_4.setTitle(_translate("MainWindow", "IPA or PAK Directory"))
        self.fld_ipa_or_pak_dir.setPlaceholderText(_translate("MainWindow", "Select IPA or PAK Directory"))
        self.btn_ipa_or_pak_dir.setText(_translate("MainWindow", "..."))
        self.groupBox_3.setTitle(_translate("MainWindow", "Project Name"))
        self.fld_proj_name.setPlaceholderText(_translate("MainWindow", "Enter Project Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.stngs), _translate("MainWindow", "Settings"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Build Time"))
        self.timeEdit.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Options"))
        self.chb_parse_log.setText(_translate("MainWindow", "Parse Log"))
        self.chb_extract_ipa.setText(_translate("MainWindow", "Extract IPA"))
        self.chb_send_to_email.setText(_translate("MainWindow", "Sent to Email"))
        self.chb_unpackpak.setText(_translate("MainWindow", "Unpak PAK"))
        self.chb_get_size.setText(_translate("MainWindow", "Get Size"))
        self.label_4.setText(_translate("MainWindow", "Parse log..."))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Send to..."))
        self.fld_rcpnts_email.setPlaceholderText(_translate("MainWindow", "Enter Recipients Emails"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ntfctn), _translate("MainWindow", "Notification"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

