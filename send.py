import smtplib
# def connect(email, password):
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     try:
#         server.login(email, password)
#         return server
#     except smtplib.SMTPAuthenticationError:
#         return False
#
# def send(email, recipients_email, msg, password):
#     connection = connect(email, password)
#     if connection is False:
#         return "Authentication is failed! Check your email or password!"
#     else:
#         return "Message is send!" if connection.sendmail(email, recipients_email, msg) else "Message don't send!"

class MailSender:
    def __init__(self, auth_email, auth_password, rcpnts_email, msg = ""):
        self.auth_email = auth_email
        self.auth_password = auth_password
        self.rcpnts_email = rcpnts_email
        self.msg = msg
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

    def send(self):
        try:
            self.server.login(self.auth_email, self.auth_password)
            try:
                self.server.sendmail(self.auth_email, self.rcpnts_email, self.msg)
                return "Message is send!"
            finally:
                self.server.quit()
        except Exception as exc: #smtplib.SMTPAuthenticationError
            return "error: {0}".format(exc)  #Authentication is failed! Check your email or password!

# a = MailSender("s.demnichenko@gmail.com", "prostosanya777", "s.demnichenko@gmail.com", "loshara")
# print(a.send())
# print(help(smtplib.SMTP_SSL))