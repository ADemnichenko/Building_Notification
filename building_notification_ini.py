import sys
import time
import smtplib
from send_message import check_build_status

from PyQt5 import QtWidgets
from UI import  building_notification


class Build_Notification_init(building_notification.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Build_Notification_init, self).__init__()
        self.setupUi(self)
        self.enter_path_btn.clicked.connect(lambda: self.enter_path.setText(pathDialog(self)))  # Select Path
        self.start_btn.clicked.connect(lambda: params_ini(self))

    #Close Event
    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtWidgets.QMessageBox.Yes |
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()

        else:
            event.ignore()

def params_ini(self):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    email = self.enter_enail.text()
    password = self.enter_enail_pass.text()
    path = self.enter_path.text()
    f_c, s_c = 0, 0

    if email != "" and path != "" and password != "":
        try:
            server.login(email, password)
            msg = True
        except smtplib.SMTPAuthenticationError:
            msg = False
        if msg:
            self.statusbar.showMessage("Authentification is true!", 1000)
            fails_count, success_count = check_build_status(path)

            while f_c <= fails_count or s_c <= success_count:
                time.sleep(60)
                f_c, s_c = check_build_status(path)
                if f_c > fails_count:
                    server.sendmail(email, email, "BUILD FAILED!")
                    break
                if s_c > success_count:
                    server.sendmail(email,email, "BUILD SUCCESS!")
                    break
        else:
            self.statusbar.showMessage("Authentification is false!", 1000)

    else:
        self.statusbar.showMessage('Fields must not be empty!', 1000)


#Select Path Dialog
def pathDialog(self):
    path = QtWidgets.QFileDialog.getOpenFileName()
    if (path[0] != ""):
        self.statusbar.showMessage('Select path: ' + list(path)[0], 1000)
        return list(path)[0]
    else:
        self.statusbar.showMessage('Path don\'t select!', 1000)

if __name__=='__main__':
    qapp = QtWidgets.QApplication(sys.argv)
    build_notify = Build_Notification_init()
    build_notify.show()
    qapp.exec_()