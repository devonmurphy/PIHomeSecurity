#!/usr/bin/env python
import os
import time
import requests
import json
import smtplib

############################################
EMAIL = "YOUR_EMAIL"
PASS = "YOUR_EMAIL_PASSWORD"
############################################

time.sleep(1)
print os.system('./ngrok http 5000 -auth="username:password" -log=stdout > ngrok.log &');

print os.system('python website.py &');

time.sleep(2)

r = requests.get('http://localhost:4040/api/tunnels/command_line')
rJson = r.json()
publicURL = rJson['public_url']

stringPublicURL = str(publicURL)
stringPublicURL = stringPublicURL[8:len(publicURL)]

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(EMAIL, PASS)

server.sendmail(EMAIL, EMAIL, stringPublicURL)
server.quit()
