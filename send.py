import smtplib
import re
import zipfile

class CheckFields:
    def __init__(self):
        self.r_email = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
        self.r_pass = re.compile(r"(^[a-zA-Z0-9+-]+$)")
    def CheckMail(self, email):
        return True if self.r_email.findall(email) else False
    def CheckPassword(self, password):
        return True if self.r_pass.findall(password) else False

class MailSender:
    def __init__(self):
        self.auth_email = ""
        self.auth_password = ""
        self.rcpnts_email = ""
        self.msg = ""
        self.check = CheckFields()

    def testConection(self, auth_email, auth_password):
        if auth_email != "" and auth_password != "":
            if self.check.CheckMail(auth_email) and self.check.CheckPassword(auth_password):
                self.auth_email = auth_email
                self.auth_password = auth_password
                self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                try:
                    self.server.login(self.auth_email, self.auth_password)
                    return "Connection is True!"
                except smtplib.SMTPAuthenticationError:
                    return "Connection is Failed!"
                finally:
                    self.server.quit()
            else:
                return "Incorrect email or password!"
        else:
            return "Email and Password fields must not be empty!"

    def send(self, auth_email, auth_password, rcpnts_email, msg):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        try:
            self.server.login(auth_email, auth_password)
            try:
                self.server.sendmail(auth_email, rcpnts_email, msg)
                return "Message is send!"
            finally:
                self.server.quit()
        except Exception as exc:
            return "error: {0}".format(exc)