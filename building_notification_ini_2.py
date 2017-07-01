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
        self.tabWidget.setCurrentWidget(self.stngs)

        # Settings
        self.settings = UserSettings()
        self.config_params = self.settings.checkSettings()
        self.fld_ipa_or_pak_dir.setText(self.config_params.get("ipa_or_pak_dir", ""))
        self.fld_proj_path.setText(self.config_params.get("project_path", ""))
        self.fld_rcpnts_email.setText(self.config_params.get("recipients_email", ""))
        self.fld_email.setText(self.config_params.get("email", ""))
        self.fld_password.setText(self.config_params.get("password", ""))
        self.fld_proj_name.setText(self.config_params.get("project_name", ""))

        #For send
        self.mail = MailSender()

        #Threading
        self.build_thread = Thread()
        # self.build_thread.signal.connect(self.parseLog, QtCore.Qt.QueuedConnection)

        #Save Data Event
        self.fld_proj_name.textChanged.connect(
            lambda: self.statusbar.showMessage(self.settings.saveSettings(project_name = self.fld_proj_name.text()), 3000))
        self.fld_ipa_or_pak_dir.textChanged.connect(
            lambda: self.statusbar.showMessage(self.settings.saveSettings(ipa_or_pak_dir = self.fld_ipa_or_pak_dir.text()), 3000))
        self.fld_proj_path.textChanged.connect(
            lambda: self.statusbar.showMessage(self.settings.saveSettings(project_path = self.fld_proj_path.text()), 3000))
        self.fld_password.textChanged.connect(
            lambda: self.statusbar.showMessage(self.settings.saveSettings(password = self.fld_password.text()), 3000))
        self.fld_email.textChanged.connect(
            lambda: self.statusbar.showMessage(self.settings.saveSettings(email = self.fld_email.text()), 3000))
        self.fld_rcpnts_email.textChanged.connect(
            lambda: self.statusbar.showMessage(self.settings.saveSettings(recipients_email = self.fld_rcpnts_email.text()), 3000))

        #Setting up events for  pressing buttons
        self.btn_start.clicked.connect(lambda: self.on_click_start())
        self.btn_cancel.clicked.connect(lambda: self.on_click_cancel())
        self.btn_connection.clicked.connect(
            lambda: self.statusbar.showMessage(self.mail.testConection(self.fld_email.text(), self.fld_password.text())))
        self.btn_proj_dir.clicked.connect(
            lambda: self.fld_proj_path.setText(self.on_click_get_path(self.fld_proj_path.text())))
        self.btn_ipa_or_pak_dir.clicked.connect(
            lambda: self.fld_ipa_or_pak_dir.setText(self.on_click_get_path(self.fld_ipa_or_pak_dir.text())))

    def on_click_start(self):
        if self.chb_extract_ipa.isChecked():
            if self.fld_ipa_or_pak_dir.text() != "":
                pass
            else:
                self.statusbar.showMessage("IPA or PAK directory field must not be empty!", 3000)
        elif self.chb_get_size.isChecked():
            if self.fld_ipa_or_pak_dir.text():
                pass
            else:
                self.statusbar.showMessage("IPA or PAK directory field must not be empty!", 3000)
        elif self.chb_parse_log.isChecked():
            if self.fld_proj_path.text() != "" and self.fld_proj_name.text() != "":
                pass
            else:
                self.statusbar.showMessage("Proj name and proj directory fields must not be empty!", 3000)
        elif self.chb_send_to_email.isChecked():
            if self.fld_email.text() != "" and self.fld_password.text() != "" and self.fld_rcpnts_email.text() != "":
                pass
            else:
                self.statusbar.showMessage("Authorization and Send to.. fields must not be empty!", 3000)
        elif self.chb_unpackpak.isChecked():
            if self.fld_proj_path.text() != "" and self.fld_ipa_or_pak_dir.text() != "":
                pass
            else:
                self.statusbar.showMessage("Proj directory and IPA or PAK fields must noyt be empty!", 3000)
        else:
            self.statusbar.showMessage("Choose options!", 3000)

    def on_click_cancel(self):
        pass

    def on_click_get_path(self, start_dir = "" ):
        return QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory", start_dir.replace("\n", ""))

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