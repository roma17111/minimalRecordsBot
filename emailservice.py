import smtplib
from email.message import EmailMessage


def send_email(text):
    msg = EmailMessage()
    msg.set_content(text)
    msg['Subject'] = 'MinimalRecords'
    msg['From'] = 'botsuperlager@gmail.com'
    msg['To'] = 'romanze1706@gmail.com'
    smtp_obj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    smtp_obj.login()
    smtp_obj.send_message(msg)
    smtp_obj.quit()
