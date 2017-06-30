from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import time
from setttings import UserSettings
from notification import check_build_status
from send import MailSender
from UI import  building_notification_2


class Build_Notification_init(building_notification_2.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Build_Notification_init, self).__init__()
        self.setupUi(self)
        self.auth = MailSender()
    #     #Set Settings
    #     self.settings = UserSettings()
    #     self.settings_params = self.settings.checkSettings()
    #     self.enter_enail.setText(self.settings_params.get("login", ""))
    #     self.enter_enail_pass.setText(self.settings_params.get("password", ""))
    #     self.enter_path_dir.setText(self.settings_params.get("directory", ""))
    #
        #Threading
        self.build_thread = Thread()
        self.build_thread.signal.connect(self.parseLog, QtCore.Qt.QueuedConnection)
    #
    #     #Set params
    #     self.auth_email = ""
    #     self.auth_password = ""
    #     self.working_dir = ""
    #     self.rcpnts_email = ""
    #     self.file_name = ""
    #     self.file_path = ""
    #     self.fails_count = 0
    #     self.sucess_count = 0
    #
        #Setting up events for  pressing click
        self.btn_connection.clicked.connect(lambda: self.on_click_test_connection())
        self.btn_proj_dir.clicked.connect(lambda: self.fld_proj_path.setText(self.getPath()))
        self.btn_ipa_or_pak_dir.clicked.connect(lambda: self.fld_ipa_or_pak_dir.setText(self.getPath()))
        self.btn_start.clicked.connect(lambda: self.on_click_start())

    def parseLog(self, signal):
        m, s = divmod(signal, 60)
        h, m = divmod(m, 60)
        self.timeEdit.setTime(QtCore.QTime(h, m, s))
        if signal % 60 == 0:
            f_c, s_c = check_build_status(self.file_path)
            if f_c > self.fails_count : build_status = "BUILD FAILED!"
            elif s_c > self.sucess_count : build_status = "BUILD SUCCESSFUL!"
            else: build_status = ""
            if build_status != "":
                sender = MailSender(self.auth_email, self.auth_password,self.rcpnts_email, build_status)
                sender.send()
                self.build_thread.terminate()
                self.start_btn.button(QtWidgets.QDialogButtonBox.Ok).setDisabled(False)

    def on_click_test_connection(self):
        if self.fld_email != "" and self.fld_password != "":
            self.statusbar.showMessage(self.auth.TestConection(self.fld_email.text(), self.fld_password.text()), 5000)
        else: self.statusbar.showMessage("Login or Password fields, must not be empty!", 5000)

    def on_click_start(self):
        if self.checkBox.isChecked() == True:
            self.build_thread.start()

    def on_click_cancel(self):
        self.start_btn.button(QtWidgets.QDialogButtonBox.Ok).setDisabled(False)
        self.build_thread.terminate()
        self.statusbar.showMessage("Canceled...", 5000)

    def getPath(self, start_dir = "" ):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory",start_dir.replace("\n", ""))
        if path != "":
            self.statusbar.showMessage("Selected: {0}".format(path))
            return path
        else:
            self.statusbar.showMessage("Path don't selected!")
            return path

    def closeEvent(self, event):
        messagebox = QtWidgets.QMessageBox()
        messagebox.setIcon(QtWidgets.QMessageBox.Question)
        messagebox.setWindowTitle('Exit')
        messagebox.setText('Are you sure, you want to quit?')
        messagebox.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        messagebox.setStyleSheet(
            "QLabel {color: rgb(203, 203, 203); }"
            "QMessageBox { background-color: rgb(81, 81, 81); }"
            "QPushButton { /* all types of tool button */\n"
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
        buttonY = messagebox.button(QtWidgets.QMessageBox.Yes)
        buttonN = messagebox.button(QtWidgets.QMessageBox.No)
        buttonN.setFixedWidth(50)
        buttonY.setFixedWidth(50)
        buttonY.setFixedHeight(15)
        buttonN.setFixedHeight(15)
        res = messagebox.exec_()
        if res == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class Thread(QtCore.QThread):
    signal = QtCore.pyqtSignal(int)
    def __init__(self):
        QtCore.QThread.__init__(self)

    def run(self):
        i = 0
        while True:
            time.sleep(1)
            self.signal.emit(i)
            i += 1
if __name__=='__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    build_notify = Build_Notification_init()
    build_notify.show()
    qapp.exec_()