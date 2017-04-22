import sys
import time
import smtplib
from setttings import checkSettings, saveSettings, resetSettings, getPath
from notification import check_build_status

from PyQt5 import QtWidgets, QtGui, QtCore
from UI import  building_notification


class Build_Notification_init(building_notification.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Build_Notification_init, self).__init__()
        self.setupUi(self)

        # Settings
        configFileName = "config.txt"
        config = checkSettings(configFileName)
        self.enter_enail.setText(config.get("login", ""))
        self.enter_enail_pass.setText(config.get("password", ""))
        self.enter_path_dir.setText(config.get("directory", ""))
        self.save_reset_btn.button(QtWidgets.QDialogButtonBox.Save).clicked.connect(lambda: saveSettings(self, configFileName))
        self.save_reset_btn.button(QtWidgets.QDialogButtonBox.Reset).clicked.connect(lambda: resetSettings(self, configFileName))
        self.enter_path_btn.clicked.connect(lambda: self.enter_path_dir.setText(getPath(self, str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")))))  # Select Path

        # Notification
        self.sel_file_btn.clicked.connect(lambda: self.enter_path_file.setText(getFileName(self)))
        self.start_btn.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(lambda: params_ini(self))
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

#Get selected file name
def getFileName(self):
    path, filter = QtWidgets.QFileDialog.getOpenFileName(self, "Open file")
    fileName = QtCore.QFileInfo(path).fileName()
    if (fileName != ""):
        self.statusbar.showMessage('Select file: ' + fileName, 1000)
        return fileName
    else:
        self.statusbar.showMessage('File don\'t select!', 1000)

def params_ini(self):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    email = self.enter_enail.text()
    recipients_email = self.enter_recipients_email.text()
    password = self.enter_enail_pass.text()
    fileName = self.enter_path_file.text()

    if recipients_email != "" and fileName != "":

        path = self.enter_path_dir.text().replace("\n", "") + "/" + fileName
        fails_count, success_count = check_build_status(path)

        try: #Check authentification
            server.login(email, password)
            msg = "Authentification is true!", True
        except smtplib.SMTPAuthenticationError:
            msg = "Authentification is false!", False
        finally:
            self.statusbar.showMessage(msg[0], 1000)
        checkAndSend(server, fails_count, success_count, path, email, recipients_email) if msg[1] is True else 0
    else:
        self.statusbar.showMessage('Recipients field must not be empty!', 1000)


#Check log and send message
def checkAndSend(server, fails_count, success_count, path, email, recipients_email):
    f_c, s_c = check_build_status(path)
    if f_c > fails_count or s_c > success_count:
        server.sendmail(email, recipients_email, "BUILD FAILED!") if f_c > fails_count else 0
        server.sendmail(email, recipients_email, "BUILD SUCCESS!") if s_c > success_count else 0
    else:
        time.sleep(60)
        checkAndSend(server,fails_count, success_count, path, email, recipients_email)

if __name__=='__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    build_notify = Build_Notification_init()
    build_notify.show()
    qapp.exec_()