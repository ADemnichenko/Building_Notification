from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import time
from setttings import UserSettings
from notification import check_build_status
from send import MailSender
from UI import  building_notification


class Build_Notification_init(building_notification.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Build_Notification_init, self).__init__()
        self.setupUi(self)

        #Set Settings
        self.settings = UserSettings()
        self.settings_params = self.settings.checkSettings()
        self.enter_enail.setText(self.settings_params.get("login", ""))
        self.enter_enail_pass.setText(self.settings_params.get("password", ""))
        self.enter_path_dir.setText(self.settings_params.get("directory", ""))

        #Threading
        self.build_thread = Thread()
        self.build_thread.signal.connect(self.parseLog, QtCore.Qt.QueuedConnection)

        #Set params
        self.auth_email = ""
        self.auth_password = ""
        self.working_dir = ""
        self.rcpnts_email = ""
        self.file_name = ""
        self.file_path = ""
        self.fails_count = 0
        self.sucess_count = 0

        #Setting up events for  pressing click
        self.save_reset_btn.button(QtWidgets.QDialogButtonBox.Save).clicked.connect(lambda: self.on_click_save())
        self.save_reset_btn.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(lambda: self.on_click_reset())
        self.enter_path_btn.clicked.connect(lambda: self.getPath())
        self.sel_file_btn.clicked.connect(lambda: self.getFileName())
        self.start_btn.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda: self.on_click_ok())
        self.start_btn.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda: self.on_click_cancel())

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

    def on_click_save(self):
        self.statusbar.showMessage(
            self.settings.saveSettings(
                self.enter_enail.text(),
                self.enter_enail_pass.text(),
                self.enter_path_dir.text()), 5000)

    def on_click_reset(self):
        if self.settings.resetSettings():
            self.statusbar.showMessage("Reset Complete!", 5000)
            self.enter_enail.setText("")
            self.enter_enail_pass.setText("")
            self.enter_path_dir.setText("")
        else:
            self.statusbar.showMessage("Reset Failed!", 5000)

    def on_click_ok(self):
        self.auth_email = self.enter_enail.text()
        self.auth_password = self.enter_enail_pass.text()
        self.working_dir = self.enter_path_dir.text()
        self.rcpnts_email = self.enter_recipients_email.text()
        self.file_name = self.enter_path_file.text()
        if self.rcpnts_email != "" and self.file_name != "" and self.auth_password != "" and self.auth_email != "":
            self.start_btn.button(QtWidgets.QDialogButtonBox.Ok).setDisabled(True)
            self.file_path = self.working_dir.replace("\n", "") + "/" + self.file_name
            self.fails_count, self.sucess_count = check_build_status(self.file_path)
            self.build_thread.start()
        else:
            return self.statusbar.showMessage("Settings and Notification fields must not be empty!", 5000)

    def on_click_cancel(self):
        self.start_btn.button(QtWidgets.QDialogButtonBox.Ok).setDisabled(False)
        self.build_thread.terminate()
        self.statusbar.showMessage("Canceled...", 5000)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtWidgets.QMessageBox.Yes |
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def getPath(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory", self.enter_path_dir.text().replace("\n", ""))
        if path != "":
            self.statusbar.showMessage('Select path: ' + path, 5000)
            return self.enter_path_dir.setText(path)
        else:
            self.statusbar.showMessage('Path don\'t select!', 5000)
            return self.enter_path_dir.setText(self.enter_path_dir.text())

    def getFileName(self):
        path, filter = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", self.enter_path_dir.text().replace("\n", ""))
        file_name = QtCore.QFileInfo(path).fileName()
        if file_name != "":
            self.statusbar.showMessage('Select file: ' + file_name, 5000)
            return self.enter_path_file.setText(file_name)
        else:
            self.statusbar.showMessage('File don\'t select!', 5000)
            return self.enter_path_file.setText(self.enter_path_file.text())

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