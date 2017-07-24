import os
import json
class UserSettings():
    def __init__(self):
        self.config_filename = "config"
        self.config_json = {}

    def saveSettings(self, toFile, **kwargs):
        if toFile is False:
            self.config_json.update(kwargs)
            return str(kwargs)
        elif toFile is True:
            with open(os.path.abspath(os.path.curdir) + "/" + self.config_filename, "w") as config:
                json.dump(self.config_json, config, indent=4)

    def checkSettings(self):
        try:
            with open(os.path.abspath(os.path.curdir) + "/" + self.config_filename, "r") as config:
                self.config_json = json.load(config)
                return self.config_json
        except FileNotFoundError:
            return {}
