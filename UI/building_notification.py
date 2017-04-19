# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/building_notification.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(334, 221)
        MainWindow.setMinimumSize(QtCore.QSize(334, 221))
        MainWindow.setMaximumSize(QtCore.QSize(334, 221))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.enter_path = QtWidgets.QLineEdit(self.frame_2)
        self.enter_path.setObjectName("enter_path")
        self.gridLayout_2.addWidget(self.enter_path, 0, 0, 1, 1)
        self.enter_path_btn = QtWidgets.QPushButton(self.frame_2)
        self.enter_path_btn.setObjectName("enter_path_btn")
        self.gridLayout_2.addWidget(self.enter_path_btn, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.start_btn = QtWidgets.QPushButton(self.frame_3)
        self.start_btn.setMinimumSize(QtCore.QSize(61, 61))
        self.start_btn.setObjectName("start_btn")
        self.gridLayout_4.addWidget(self.start_btn, 0, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_3, 1, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.enter_enail = QtWidgets.QLineEdit(self.frame)
        self.enter_enail.setObjectName("enter_enail")
        self.gridLayout.addWidget(self.enter_enail, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.enter_enail_pass = QtWidgets.QLineEdit(self.frame)
        self.enter_enail_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.enter_enail_pass.setObjectName("enter_enail_pass")
        self.gridLayout.addWidget(self.enter_enail_pass, 1, 1, 1, 1)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Building Notification"))
        self.enter_path_btn.setText(_translate("MainWindow", "Select Path"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.label.setText(_translate("MainWindow", "Enter Email:"))
        self.label_2.setText(_translate("MainWindow", "Enter Password:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

