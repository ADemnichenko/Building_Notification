from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import time
from setttings import UserSettings
from notification import check_build_status, buildTime, checkFields
from send import MailSender
from UI import  building_notification_3
from test import UnpakingProject

class Build_Notification_init(building_notification_3.Ui_MainWindow, QtWidgets.QMainWindow):
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

        #Set params
        self.build_time = []
        self.fails_count = 0
        self.log_file_path = ""
        self.sucess_count = 0
        self.checkbox_check = []
        self.extract_ipa_check = False
        self.send_msg = ""

        #Unpucking
        self.unpack = UnpakingProject(self.fld_ipa_or_pak_dir.text().strip())

        #For send
        self.mail = MailSender()

        #Threading
        self.parse_log = Thread()
        self.send = Thread()
        self.parse_log.signal.connect(self.parseLog, QtCore.Qt.QueuedConnection)
        self.parse_log.finished.connect(self.sendMsg, QtCore.Qt.QueuedConnection)

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
        self.chb_parse_log.stateChanged.connect(lambda: self.checkboxStateChanged())
        self.chb_send_to_email.stateChanged.connect(lambda: self.checkboxStateChanged())
        self.chb_get_size.stateChanged.connect(lambda: self.checkboxStateChanged())
        self.chb_extract_ipa.stateChanged.connect(lambda: self.checkboxStateChanged())

        self.btn_start.clicked.connect(lambda: self.on_click_start())
        self.btn_cancel.clicked.connect(lambda: self.on_click_cancel())
        self.btn_connection.clicked.connect(
            lambda: self.statusbar.showMessage(self.mail.testConection(self.fld_email.text(), self.fld_password.text())))
        self.btn_proj_dir.clicked.connect(
            lambda: self.fld_proj_path.setText(self.on_click_get_path(self.fld_proj_path.text())))
        self.btn_ipa_or_pak_dir.clicked.connect(
            lambda: self.fld_ipa_or_pak_dir.setText(self.on_click_get_path(self.fld_ipa_or_pak_dir.text())))

    def checkboxStateChanged(self):
        self.checkbox_check = self.chb_parse_log.checkState(), \
                              self.chb_send_to_email.checkState(), \
                              self.chb_get_size.checkState(), \
                              self.chb_extract_ipa.checkState()

    def fieldsControl(self):
        if self.chb_parse_log.isChecked():
            if checkFields(self.fld_proj_name.text().strip(), self.fld_proj_path.text().strip()) is False:
                self.statusbar.showMessage("Proj name and proj dir fields must not be empty!", 3000)
                return False
            else:
                result = True
        if self.chb_send_to_email.isChecked():
            if checkFields(self.fld_email.text().strip(), self.fld_password.text().strip(), self.fld_rcpnts_email.text().strip()) is False:
                self.statusbar.showMessage("Auth and Rcpnts fields must not be empty!", 3000)
                return False
            else:
                result = True
        if self.chb_extract_ipa.isChecked():
            if checkFields(self.fld_ipa_or_pak_dir.text().strip(), self.fld_proj_path.text().strip()) is False:
                self.statusbar.showMessage("IPA and proj dir fields must not be empty!", 3000)
                return False
            else:
                result = True
        if self.chb_get_size.isChecked():
            if checkFields(self.fld_ipa_or_pak_dir.text().strip()) is False:
                self.statusbar.showMessage("IPA or Pak field must not be empty!", 3000)
                return False
            else:
                result = True
        return result

    def sendMsg(self):
        if self.chb_send_to_email.isChecked():
            if self.send_msg != "":
                status = self.mail.send(self.fld_email.text(),
                               self.fld_password.text(),
                               self.fld_rcpnts_email.text(),
                               self.send_msg)
                self.statusbar.showMessage(status, 3000)

    def parseLog(self, signal):
        h,m,s = buildTime(signal)
        self.timeEdit.setTime(QtCore.QTime(h, m, s))
        if signal % 60 == 0:
            f_c, s_c = check_build_status(self.log_file_path)
            if f_c > self.fails_count : build_status = "BUILD FAILED!"
            elif s_c > self.sucess_count : build_status = "BUILD SUCCESSFUL!"
            else: build_status = ""
            if build_status != "":
                self.send_msg = "Build Status: {0}\n " \
                                "Build Time: {1}\n".format(build_status, self.timeEdit.text())
                self.parse_log.terminate()
                self.btn_start.setDisabled(False)


    def on_click_start(self):
        if 2 in self.checkbox_check:
            if self.fieldsControl():
                if self.chb_parse_log.isChecked():
                    file, directory, checker = self.unpack.ResearchFile("{0}/Saved/Logs".format(self.fld_proj_path.text().strip()), ".log")
                    if checker:
                        self.log_file_path = "{0}/{1}".format(directory, file)
                        self.fails_count, self.sucess_count = check_build_status(self.log_file_path)
                        self.btn_start.setDisabled(True)
                        self.parse_log.start()
                    else:
                        self.statusbar.showMessage("Log file not found!", 3000)
        else:
            self.statusbar.showMessage("Select option!", 3000)

    def on_click_cancel(self):
        self.btn_start.setDisabled(False)
        self.parse_log.terminate()
        self.statusbar.showMessage("Canceled...", 5000)

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