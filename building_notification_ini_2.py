from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import time
import os
import zipfile
from subprocess import call
from setttings import UserSettings
from notification import check_build_status, checkFields
from send import MailSender
from UI import  building_notification_3

class Build_Notification_init(building_notification_3.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(Build_Notification_init, self).__init__()
        self.setupUi(self)
        self.tabWidget.setCurrentWidget(self.stngs)

        self.chb_get_size.setChecked(True)
        self.chb_send_to_email.setChecked(True)
        self.chb_extract_ipa.setChecked(True)
        self.chb_unpack_pak.setChecked(True)
        self.checkBoxStates(True)

        # Settings
        self.mail = MailSender()
        self.options = Options(self)
        self.settings = UserSettings()
        self.config = self.settings.checkSettings()
        self.fld_ipa_or_pak_dir.setText(self.config.get("ipa_or_pak_dir", ""))
        self.fld_proj_path.setText(self.config.get("project_path", ""))
        self.fld_rcpnts_email.setText(self.config.get("recipients_email", ""))
        self.fld_email.setText(self.config.get("email", ""))
        self.fld_password.setText(self.config.get("password", ""))
        self.fld_proj_name.setText(self.config.get("project_name", ""))
        self.fld_unrealpak_dir.setText(self.config.get("unreal_pak_dir", ""))

        #Threading
        self.parse_log = Thread()
        self.parse_log.signal.connect(self.options.parseStart, QtCore.Qt.QueuedConnection)

        #Save Data Event

        self.fld_proj_name.textChanged.connect(
            lambda: self.statusbar.showMessage(self.settings.saveSettings(False, project_name = self.fld_proj_name.text()), 3000))
        self.fld_ipa_or_pak_dir.textChanged.connect(
            lambda: self.statusbar.showMessage(self.settings.saveSettings(False, ipa_or_pak_dir = self.fld_ipa_or_pak_dir.text()), 3000))
        self.fld_proj_path.textChanged.connect(
            lambda: self.statusbar.showMessage(self.settings.saveSettings(False, project_path = self.fld_proj_path.text()), 3000))
        self.fld_password.textChanged.connect(
            lambda: self.statusbar.showMessage(self.settings.saveSettings(False, password = self.fld_password.text()), 3000))
        self.fld_email.textChanged.connect(
            lambda: self.statusbar.showMessage(self.settings.saveSettings(False, email = self.fld_email.text()), 3000))
        self.fld_rcpnts_email.textChanged.connect(
            lambda: self.statusbar.showMessage(self.settings.saveSettings(False, recipients_email = self.fld_rcpnts_email.text()), 3000))
        self.fld_unrealpak_dir.textChanged.connect(
            lambda: self.statusbar.showMessage(self.settings.saveSettings(False, unreal_pak_dir = self.fld_unrealpak_dir.text()), 3000))

        #Setting up events for  pressing buttons
        self.chb_parse_log.stateChanged.connect(lambda: self.checkboxParseLogStateChanged())
        self.btn_start.clicked.connect(lambda: self.on_click_start())
        self.btn_cancel.clicked.connect(lambda: self.on_click_cancel())
        self.btn_connection.clicked.connect(
            lambda: self.statusbar.showMessage(self.mail.testConection(self.fld_email.text(), self.fld_password.text()), 3000))
        self.btn_proj_dir.clicked.connect(
            lambda: self.fld_proj_path.setText(self.on_click_get_path(self.fld_proj_path.text())))
        self.btn_unrealpak_dir.clicked.connect(
            lambda: self.fld_unrealpak_dir.setText(self.on_click_get_path(self.fld_unrealpak_dir.text())))
        self.btn_ipa_or_pak_dir.clicked.connect(
            lambda: self.fld_ipa_or_pak_dir.setText(self.on_click_get_path(self.fld_ipa_or_pak_dir.text())))

    def checkboxParseLogStateChanged(self):
        if self.chb_parse_log.isChecked():
            self.checkBoxStates(False)
        else:
            self.checkBoxStates(True)

    def fieldsControl(self):
        if self.chb_parse_log.isChecked():
            if checkFields(self.fld_proj_name.text().strip(), self.fld_proj_path.text().strip()) is False:
                self.statusbar.showMessage("Project name and Game Directory fields must not be empty!", 3000)
                return False
            else:
                result = True
        if self.chb_send_to_email.isChecked():
            if checkFields(self.fld_email.text().strip(), self.fld_password.text().strip(), self.fld_rcpnts_email.text().strip()) is False:
                self.statusbar.showMessage("Auth and Recipients fields must not be empty!", 3000)
                return False
            else:
                result = True
        if self.chb_extract_ipa.isChecked():
            if checkFields(self.fld_ipa_or_pak_dir.text().strip(), self.fld_proj_path.text().strip()) is False:
                self.statusbar.showMessage("IPA and Game directory fields must not be empty!", 3000)
                return False
            else:
                result = True
        if self.chb_get_size.isChecked():
            if checkFields(self.fld_ipa_or_pak_dir.text().strip()) is False:
                self.statusbar.showMessage("IPA or Pak fields must not be empty!", 3000)
                return False
            else:
                result = True
        if self.chb_unpack_pak.isChecked():
            if checkFields(self.fld_ipa_or_pak_dir.text().strip(), self.fld_unrealpak_dir.text().strip()) is False:
                self.statusbar.showMessage("IPA/PAK or UnrealPak directory fields must not be empty!", 3000)
                return False
            else:
                result = True
        return result

    def checkBoxStates(self, state):
        self.chb_send_to_email.setDisabled(state)
        self.chb_get_size.setDisabled(state)
        self.chb_extract_ipa.setDisabled(state)
        self.chb_unpack_pak.setDisabled(state)

    def on_click_start(self):
        if self.chb_parse_log.isChecked():
            if self.fieldsControl():
                self.settings.saveSettings(True,)
                self.options.resetParams()
                if self.options.researchFile("{0}/Saved/Logs".format(self.fld_proj_path.text().strip()), ".log"):
                    self.btn_start.setDisabled(True)
                    self.parse_log.start()
                    self.chb_parse_log.setDisabled(True)
                    self.checkBoxStates(True)
                else:
                    self.statusbar.showMessage("Log file not found!", 3000)
        else:
            self.statusbar.showMessage("Select option!", 3000)

    def on_click_cancel(self):
        self.btn_start.setDisabled(False)
        self.parse_log.terminate()
        self.options.resetParams()
        self.chb_parse_log.setDisabled(False)
        self.checkBoxStates(False)
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

class Options():
    def __init__(self, copyUiClass):
        self.file_path = ""
        self.copyUiClass = copyUiClass
        self.fails_count, self.sucess_count = "", ""
        self.build_status = ""
        self.send_msg = ""
        self.size_statistic = ""

    def resetParams(self):
        self.send_msg = ""
        self.build_status = ""
        self.file_path = ""
        self.fails_count, self.sucess_count = "", ""

    def researchFile(self, path, extension = ""):
        result = False
        for dir, subdirs, files in os.walk(path):
            for filename in files:
                if filename.endswith(extension):
                    result = True
                    self.file_path = "{0}/{1}".format(dir, filename)
        return result

    def buildTime(self, val):
        m, s = divmod(val, 60)
        h, m = divmod(m, 60)
        return self.copyUiClass.timeEdit.setTime(QtCore.QTime(h, m, s))

    def parseStart(self, signal):
        self.buildTime(signal)
        if self.fails_count == "" and self.sucess_count == "":
            self.fails_count, self.sucess_count = check_build_status(self.file_path)
        else:
            if signal % 60 == 0:
                    f_c, s_c = check_build_status(self.file_path)
                    if f_c > self.fails_count : self.build_status = False
                    elif s_c > self.sucess_count : self.build_status = True
                    if self.build_status is True:
                        self.send_msg = "Build Status -  Build Succesful!\n" \
                                        "Build Time -  {0}\n".format(self.copyUiClass.timeEdit.text())
                        self.copyUiClass.parse_log.terminate()
                        self.copyUiClass.btn_start.setDisabled(False)
                        self.extractIPA()
                        self.unpackPAK()
                        self.getSize(".ipa")
                        self.getSize(".pak")
                        self.getPackageSize()
                        self.sendMessage()
                        self.copyUiClass.checkBoxStates(False)

                    elif self.build_status is False:
                        self.copyUiClass.parse_log.terminate()
                        self.copyUiClass.btn_start.setDisabled(False)
                        self.send_msg = "Build Status -  Build False!\n" \
                                        "Build Time -  {0}\n".format(self.copyUiClass.timeEdit.text())
                        self.sendMessage()
                        self.copyUiClass.checkBoxStates(False)

    def unpackPAK(self):
        if self.copyUiClass.chb_unpack_pak.isChecked():
            pak_folder_name = "unpackPAK"
            if self.researchFile(self.copyUiClass.fld_ipa_or_pak_dir.text().strip(), ".pak") is True:
                if os.name == "posix":
                    os.system("{0}/UnrealPak {1} -Extract {2}/{3}".format(
                        self.copyUiClass.fld_unrealpak_dir.text().strip().replace(" ", "\ "),
                        self.file_path,
                        self.copyUiClass.fld_ipa_or_pak_dir.text().strip(),
                        pak_folder_name))
                if os.name == "nt":
                    os.system("\"{0}/UnrealPak.exe\" {1} -Extract {2}/{3}".format(
                        self.copyUiClass.fld_unrealpak_dir.text().strip(),
                        self.file_path,
                        self.copyUiClass.fld_ipa_or_pak_dir.text().strip(),
                        pak_folder_name))

    def extractIPA(self):
        if self.copyUiClass.chb_extract_ipa.isChecked():
            ipa_folder_name = "extractIPA"
            if self.researchFile(self.copyUiClass.fld_ipa_or_pak_dir.text().strip(), ".ipa") is True:
                zip_file = zipfile.ZipFile("{0}".format(self.file_path), 'r')
                zip_file.extractall("{0}/{1}".format(self.copyUiClass.fld_ipa_or_pak_dir.text().strip(), ipa_folder_name))
                zip_file.close()

    def getPackageSize(self):
        total_size = 0
        if self.copyUiClass.chb_get_size.isChecked():
            for dirpath, dirnames, filenames in os.walk("{0}/unpackPAK".format(self.copyUiClass.fld_ipa_or_pak_dir.text().strip())):
                if dirpath.find("Content/git Packages") != -1:
                    for dirname in os.listdir(dirpath):
                        for drp, drn, fn in os.walk("{0}/{1}".format(dirpath, dirname)):
                            for f in fn:
                                fp = os.path.join(drp, f)
                                total_size += os.path.getsize(fp)
                        self.size_statistic += self.size_statistic.join("{0} = {1}Mb\n".format(dirname, total_size / 1000000))
                        total_size = 0
                    break
            self.send_msg += "{0}\n".format(self.size_statistic)
            self.size_statistic = ""

    def getSize(self, extension):
        if self.copyUiClass.chb_get_size.isChecked():
            for dirpath, dirnames, filenames in os.walk("{0}".format(self.copyUiClass.fld_ipa_or_pak_dir.text().strip())):
                for f in filenames:
                    if f.endswith(extension):
                        fp = os.path.join(dirpath, f)
                        size = os.path.getsize(fp)
                        self.size_statistic += self.size_statistic.join(
                            "{0} size - {1}Mb".format(f, size / 1000000))
            self.send_msg += "{0}\n".format(self.size_statistic)
            self.size_statistic = ""

    def sendMessage(self):
        if self.copyUiClass.chb_send_to_email.isChecked():
            if self.send_msg != "":
                self.copyUiClass.statusbar.showMessage(self.copyUiClass.mail.send(
                    self.copyUiClass.fld_email.text(),
                    self.copyUiClass.fld_password.text(),
                    self.copyUiClass.fld_rcpnts_email.text(),
                    self.send_msg), 3000)
        else:
            with open("log.txt", "w") as log:
                log.write(self.send_msg)

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