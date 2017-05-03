import sys
import threading
import time

from setttings import checkSettings, saveSettings, resetSettings
from notification import check_build_status
from send import connect, send

from PyQt5 import QtWidgets, QtGui, QtCore
from UI import  building_notification

class Build_Notification_init(building_notification.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Build_Notification_init, self).__init__()
        self.setupUi(self)

        # Settings
        configFileName = "config.txt"
        checkSettings(self, configFileName)

        self.save_reset_btn.button(QtWidgets.QDialogButtonBox.Save).clicked.connect(lambda: saveSettings(self, configFileName))
        self.save_reset_btn.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(lambda: resetSettings(self, configFileName))
        self.enter_path_btn.clicked.connect(lambda: getPath(self))

        # Notification
        self.sel_file_btn.clicked.connect(lambda: getFileName(self))
        self.start_btn.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda: self.statusbar.showMessage(
            params_ini(
                        self.enter_enail.text(),
                        self.enter_recipients_email.text(),
                        self.enter_enail_pass.text(),
                        self.enter_path_file.text(),
                        self.enter_path_dir.text()
                       ), 5000))
        self.start_btn.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(lambda: params_ini(self))
    #Close Event
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtWidgets.QMessageBox.Yes |
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def params_ini(email, r_email, password, fileName, path_dir):

    if r_email != "" and fileName != "" and password != "" and fileName != "":

        path = path_dir.replace("\n", "") + "/" + fileName
        fails_count, success_count = check_build_status(path)
        thr = threading.Thread(target=checkAndSend, args=(password, fails_count, success_count, path, email, r_email)).start()
            # return 'Authentication is failed! Check your email or password!'
    else:
        return 'Settings and Notification fields must not be empty!'

#Check log and send message
def checkAndSend(password, fails_count, success_count, path, email, recipients_email):
    f_c, s_c = check_build_status(path)
    if f_c > fails_count:
        return send(email, recipients_email, "BUILD FAILED!", password)
    elif s_c > success_count:
        return send(email, recipients_email, "BUILD SUCCESSFUL!", password)
    else:
        for i in range(60):
            time.sleep(1)
            print(str(i))
        checkAndSend(password,fails_count, success_count, path, email, recipients_email)

#Select path
def getPath(self):
    path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory", self.enter_path_dir.text().replace("\n", ""))
    if path != "":
        self.statusbar.showMessage('Select path: ' + path, 5000)
        return self.enter_path_dir.setText(path)
    else:
        self.statusbar.showMessage('Path don\'t select!', 5000)
        return self.enter_path_dir.setText(self.enter_path_dir.text())

#Get selected file name
def getFileName(self):
    path, filter = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", self.enter_path_dir.text().replace("\n", ""))
    fileName = QtCore.QFileInfo(path).fileName()
    if fileName != "":
        self.statusbar.showMessage('Select file: ' + fileName, 5000)
        return self.enter_path_file.setText(fileName)
    else:
        self.statusbar.showMessage('File don\'t select!', 5000)
        return self.enter_path_file.setText(self.enter_path_file.text())



if __name__=='__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    build_notify = Build_Notification_init()
    build_notify.show()
    qapp.exec_()