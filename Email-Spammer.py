# -*- coding: utf-8 -*-

import smtplib, time
from datetime import datetime

n = 1
interval = int(input("Enter the minute-interval for the email to be sent\n > "))

email = input("Enter your email address\n > ")
destination = input("Enter the email address of the target\n > ")
password = input("Enter your email password\n >  ")
    
subject = ""  #Enter your subject

msg = """ Enter your message """

email_text = f"Subject: {subject}\n\n{msg}"


while True:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email, password)
    server.sendmail(email, destination, email_text.encode("utf-8"))
    t = datetime.now()
    t = t.strftime("%H:%M:%S")
    print(f"[ + ] {t} Email number {n} sent successfully to {destination}.")
    n += 1
    server.close()
    time.sleep(interval*60)
  
