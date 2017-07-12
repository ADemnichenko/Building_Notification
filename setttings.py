import os

class UserSettings():
    def __init__(self):
        self.err_msg1 = "Fields must not be empty!"
        self.err_msg2 = "Incorrectly login or password!"
        self.config_filename = "config.txt"
        self.config_params = {
            "project_name" : "",
            "ipa_or_pak_dir": "",
            "project_path": "",
            "password": "",
            "email": "",
            "recipients_email": ""
        }

    def saveSettings(self, **kwargs):
        for k in kwargs:
            self.config_params[k] = kwargs[k]
            with open(os.path.abspath(os.path.curdir) + "/" + self.config_filename, "w") as config:
                for key in self.config_params:
                    config.write(key + " = " + self.config_params.get(key).replace("\n", "") + "\n")
                return kwargs.get(k)


    def checkSettings(self):
        try:
            with open(os.path.abspath(os.path.curdir) + "/" + self.config_filename, "r") as config:
                for el in config:
                    if el.find("ipa_or_pak_dir = ") != -1:
                        self.config_params["ipa_or_pak_dir"] = el.replace("ipa_or_pak_dir = ", "")
                    if el.find("recipients_email = ") != -1:
                        self.config_params["recipients_email"] = el.replace("recipients_email = ", "")
                    if el.find("email = ") != -1:
                        self.config_params["email"] = el.replace("email = ", "")
                    if el.find("project_path = ") != -1:
                        self.config_params["project_path"] = el.replace("project_path = ", "")
                    if el.find("project_name = ") != -1:
                        self.config_params["project_name"] = el.replace("project_name = ", "")
                    if el.find("password = ") != -1:
                        self.config_params["password"] = el.replace("password = ", "")
                return self.config_params
        except FileNotFoundError:
            return {}