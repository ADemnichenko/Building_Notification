import smtplib
import re

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

    def send(self):
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        try:
            self.server.login(self.auth_email, self.auth_password)
            try:
                self.server.sendmail(self.auth_email, self.rcpnts_email, self.msg)
                return "Message is send!"
            finally:
                self.server.quit()
        except Exception as exc: #smtplib.SMTPAuthenticationError
            return "error: {0}".format(exc)  #Authentication is failed! Check your email or password!


# class MailSender:
#     def __init__(self, auth_email, auth_password, rcpnts_email, msg = ""):
#         self.auth_email = auth_email
#         self.auth_password = auth_password
#         self.rcpnts_email = rcpnts_email
#         self.msg = msg
#         self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     def send(self):
#         try:
#             self.server.login(self.auth_email, self.auth_password)
#             try:
#                 self.server.sendmail(self.auth_email, self.rcpnts_email, self.msg)
#                 return "Message is send!"
#             finally:
#                 self.server.quit()
#         except Exception as exc: #smtplib.SMTPAuthenticationError
#             return "error: {0}".format(exc)  #Authentication is failed! Check your email or password!
