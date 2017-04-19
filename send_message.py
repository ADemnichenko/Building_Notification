import smtplib

# def send_message(email, password):
#     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#     try :
#         server.login(email, password)
#     except smtplib.SMTPAuthenticationError:
#         return "Authentification is failed!"
#     else:
#         server.sendmail(email, email, "BUILD SUCCESS!!")
#         return "Authentification is complete!"
#     server.quit()


# def check_build_status(path):
#     txt = open(path)
#     for str in txt:
#         if str.find("Automation.Execute: BUILD SUCCESSFUL") != -1:
#             return True
#     txt.close()


def check_build_status(path):
    log = open(path)
    fails_counter = 0
    success_counter = 0

    for str in log:
        success_counter += 1 if str.find("BUILD SUCCESSFUL") != -1 else 0
        fails_counter += 1 if str.find("BUILD FAILED") != -1 else 0

    log.close()
    return fails_counter, success_counter

