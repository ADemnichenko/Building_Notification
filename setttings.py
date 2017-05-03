import os
#Save Settings
def saveSettings(self, fileName):
    login = self.enter_enail.text()
    password = self.enter_enail_pass.text()
    dir = self.enter_path_dir.text()
    if login != "" and password != "" and dir != "":
        params = {"login" : str(login), "password" : str(password), "directory" : str(dir)}
        with open(os.path.abspath(os.path.curdir) + "/" + fileName, "w") as config:
            for el in params:
                config.write(el+"=" + params.get(el) + "\n")
        self.statusbar.showMessage("Save", 1000)
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