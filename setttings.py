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
        return self.statusbar.showMessage("Save", 1000)
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
def checkSettings(fileName):
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
            return params
    except FileNotFoundError:
        return params

#Select path
def getPath(self, path):
    if path != "":
        self.statusbar.showMessage('Select path: ' + list(path)[0], 1000)
        return path
    else:
        self.statusbar.showMessage('Path don\'t select!', 1000)