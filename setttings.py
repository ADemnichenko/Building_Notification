import os
import re

class CheckFields:
    def __init__(self):
        self.r_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        self.r_pass = re.compile(r"(^[a-zA-Z0-9+-]+$)")

    def CheckMail(self, email):
            if self.r_email.findall(email):
                return True
            else:
                return False

    def CheckPassword(self, password):
            if self.r_pass.findall(password):
                return True
            else:
                return False

class UserSettings(CheckFields):
    def __init__(self):
        self.err_msg1 = "Fields must not be empty!"
        self.err_msg2 = "Incorrectly login or password!"
        self.params = {}

    def saveSettings(self, auth_email, auth_password, working_dir = "", file_name = "config"):
        c_m = self.CheckMail(auth_email)
        c_p = self.CheckPassword(auth_password)

        if c_m and c_p:
            if auth_email != "" and auth_password != "":
                self.params = {"login": str(auth_email), "password": str(auth_password), "directory": str(working_dir)}
                with open(os.path.abspath(os.path.curdir) + "/" + file_name, "w") as config:
                    for el in self.params:
                        return True if config.write(el + "=" + self.params.get(el) + "\n") else 0
            else:
                return self.err_msg1
        else:
            return self.err_msg2

    def resetSettings(self, file_name = "config"):
        with open(os.path.abspath(os.path.curdir) + "/" + file_name, "w") as config:
            return True if config.write("") else 0

    def checkSettings(self, file_name = "config"):
        self.params = {}
        try:
            with open(os.path.abspath(os.path.curdir) + "/" + file_name, "r") as config:
                for el in config:
                    if el.find("login=") != -1:
                        self.params["login"] = el.replace("login=", "")
                    if el.find("password=") != -1:
                        self.params["password"] = el.replace("password=", "")
                    if el.find("directory=") != -1:
                        self.params["directory"] = el.replace("directory=", "")
                return self.params
        except FileNotFoundError:
            return self.params


#Save Settings
def saveSettings(self, fileName):

    mail = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    pas = re.compile(r"(^[a-zA-Z0-9+-]+$)")

    login = self.enter_enail.text()
    password = self.enter_enail_pass.text()
    dir = self.enter_path_dir.text()

    if login != "" and password != "" and dir != "":
        if mail.findall(self.enter_enail.text()) and pas.findall(self.enter_enail_pass.text()):
            params = {"login" : str(login), "password" : str(password), "directory" : str(dir)}
            with open(os.path.abspath(os.path.curdir) + "/" + fileName, "w") as config:
                for el in params:
                    config.write(el+"=" + params.get(el) + "\n")
            self.statusbar.showMessage("Save", 1000)
        else:
            self.statusbar.showMessage("Incorrectly login or password!", 1000)
    else:
        self.statusbar.showMessage("Fields must not be empty!", 1000)

#Reset Settings
def resetSettings(self, fileName):
    with open(os.path.abspath(os.path.curdir) + "/" + fileName, "w") as config:
        config.write("")
    self.enter_enail.setText("")
    self.enter_enail_pass.setText("")
    self.enter_path_dir.setText("")
    self.statusbar.showMessage("Reset", 1000)

#Check Settings
def checkSettings(self, fileName):
    params = {}
    try:
        with open(os.path.abspath(os.path.curdir) + "/" + fileName, "r") as config:
            for el in config:
                if el.find("login=") != -1:
                    params["login"] = el.replace("login=", "")
                if el.find("password=") != -1:
                    params["password"] = el.replace("password=", "")
                if el.find("directory=") != -1:
                    params["directory"] = el.replace("directory=", "")
            self.enter_enail.setText(params.get("login", ""))
            self.enter_enail_pass.setText(params.get("password", ""))
            self.enter_path_dir.setText(params.get("directory", ""))
    except FileNotFoundError:
        return params