# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 22:52:33 2020

@author: Yifan Ren
"""

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import time

def send_email(my_receiver, subject, body):
    ret=True
    try:
        my_sender = 'renyifan@yifan-ren.com'
        password = 'WLrng5A4gHGyCWcD' # Invalid, just for example
        smtp_server = 'smtp.exmail.qq.com' #ServerAdd
        msg=MIMEText(body,'plain','utf-8')#Body Content
        msg['From']=formataddr(["xx",my_sender])#From
        msg['To']=formataddr(["xx",my_receiver])#To        
        msg['Subject']=subject #Subject
        server = smtplib.SMTP_SSL(smtp_server, 465)
        server.login(my_sender, password)
        server.sendmail(my_sender, [my_receiver], msg.as_string()) #发送地址需与登陆的邮箱一致
        server.quit()
    except Exception:  
        ret=False
    return ret

def main():
    im = False
    while im == False:
        im = send_email(my_receiver, subject, body)
        time.sleep(2)
