import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    content = ssl.create_default_context()
    user_email = "rajaachandramohan@gmail.com"
    pass1 = os.getenv("password")
    receiver = "rajaachandramohan@gmail.com"
    with smtplib.SMTP_SSL(host, port, context=content) as server:
        server.login(user_email, pass1)
        server.sendmail(user_email, receiver, message)


