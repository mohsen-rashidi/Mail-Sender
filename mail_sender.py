username= 'rashidi.lbo@gmail.com'
password = ''
server = 'smtp.gmail.com:587'

import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def create_msg(to_addr, from_addr='', subject=''):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['To'] = to_addr
    msg['From'] = from_addr
    return msg

def send_mail(smtp_server, username, password, msg):
    server = smtplib.SMTP(smtp_server)
    server.starttls()
    server.ehlo()
    server.login(username, password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()

def compose_mail(address, subject, body):
    msg = create_msg(address, subject = subject)
    with open(sys.argv[1]) as f:
        while True:
            line = f.readline()
            part = MIMEText(line, 'html')
            msg.attach(part)
            if len(line) == 0:
                break
    send_mail(server, username, password, msg)
    print('mail sent!')

compose_mail('rashidi.lbo@hotmail.com', 'it`s a test', sys.argv[1])
