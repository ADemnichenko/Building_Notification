import os
import re

class CheckFields:
    def __init__(self):
        self.r_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        self.r_pass = re.compile(r"(^[a-zA-Z0-9+-]+$)")

    def CheckMail(self, email):
        return True if self.r_email.findall(email) else False

    def CheckPassword(self, password):
        return True if self.r_pass.findall(password) else False

class UserSettings():
    def __init__(self):
        self.err_msg1 = "Fields must not be empty!"
        self.err_msg2 = "Incorrectly login or password!"
        self.params = {}
    def saveSettings(self, auth_email, auth_password, working_dir = "", file_name = "config.txt"):
        if auth_email == "" or auth_password == "":
            return self.err_msg1
        else:
            f_check = CheckFields()
            if f_check.CheckMail(auth_email) and f_check.CheckPassword(auth_password):
                self.params = {"login": str(auth_email), "password": str(auth_password), "directory": str(working_dir)}
                with open(os.path.abspath(os.path.curdir) + "/" + file_name, "w") as config:
                    for el in self.params:
                        config.write(el + "=" + self.params.get(el) + "\n")
                    return "Save Complete!"
            else:
                return self.err_msg2
    def resetSettings(self, file_name = "config.txt"):
            with open(os.path.abspath(os.path.curdir) + "/" + file_name, "w") as config:
                config.write("")
            return True
    def checkSettings(self, file_name = "config.txt"):
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