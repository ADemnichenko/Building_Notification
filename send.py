import smtplib

def connect(email, password):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    try:
        server.login(email, password)
        return server
    except smtplib.SMTPAuthenticationError:
        return False

def send(email, recipients_email, msg, password):
    connection = connect(email, password)
    if connection is False:
        return "Authentication is failed! Check your email or password!"
    else:
        return "Message is send!" if connection.sendmail(email, recipients_email, msg) else "Message don't send!"

