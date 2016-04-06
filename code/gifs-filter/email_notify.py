#!/usr/bin/env python

"""
    Notify program finishing with email

    *.py "msg"
"""
import smtplib
import sys
import socket

app_name = 'GIF Filtering'
hostname = socket.gethostname()
import os
cwd = os.getcwd()

g_config = {
    'HOST': 'smtp.gmail.com',
    'port': 587,
    'FROM':  '"%s ALERT" <m9Bb7voPjTEC@gmail.com>' % app_name,
    'TO': 'raingomm@gmail.com',
    'SUBJECT':'New Notification Event From [%s]' % app_name,
    'username': 'm9Bb7voPjTEC@gmail.com',
    'pwd': 'Rq3TdwTs7M7gQfWz',
        }

def send_mail(msg, config = None):

    if not config:
        config = g_config

    session = smtplib.SMTP(config['HOST'], config['port'])
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(config['username'], config['pwd'])

    headers = ["from: " + config['FROM'], "subject: " + config['SUBJECT'], "to: " + config['TO'], "mime-version: 1.0", "content-type: text/html"]
    headers = "\r\n".join(headers)

    msg = msg + '\r\n\r\n from ' + hostname + ' \r\n\r\n at ' + cwd

    session.sendmail(config['FROM'], config['TO'], headers + "\r\n\r\n" + msg)

def main():
    if len(sys.argv) == 2:
        send_mail(sys.argv[1])

if __name__ == "__main__":
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
