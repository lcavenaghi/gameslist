from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib


def send_mail(message):
    try:
        smtp = smtplib.SMTP(os.getenv("SMTP_SERVER"), 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(os.getenv("SMTP_USER_EMAIL"),
                   os.getenv("SMTP_USER_PASSWORD"))
        smtp.send_message(message)
        smtp.close()
        return True
    except Exception as e:
        print('Error ao enviar o email.' + str(e))
        return False


def get_message(subject, to, message):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['To'] = to
    msg['From'] = os.getenv("SMTP_USER_EMAIL")
    msg.attach(MIMEText(message, 'html'))

    return msg
