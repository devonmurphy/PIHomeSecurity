#!/usr/bin/env python

import os
import time
import requests
import json
import smtplib

############################################
EMAIL = "YOUR_GMAIL_ACCOUNT"
PASS = "GMAIL_PASSWORD"
WEBSITE_USERNAME = "username"
WEBSITE_PASSWORD = "password"
############################################

directory = os.path.dirname(os.path.realpath(__file__))
print directory

time.sleep(10)
os.system(directory + '/ngrok http 8080'+' -auth="'+WEBSITE_USERNAME+':'+WEBSITE_PASSWORD+'" -log=stdout > /dev/null &')
time.sleep(2)
os.system('sudo -u pi '+directory + '/vlc-start-stream &')
r = requests.get('http://localhost:4040/api/tunnels/command_line')
rJson = r.json()
publicURL = rJson['public_url']

stringPublicURL = str(publicURL)
stringPublicURL = stringPublicURL[8:len(publicURL)]

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(EMAIL, PASS)

server.sendmail(EMAIL, EMAIL, '\nhttp://'+stringPublicURL+'/stream')
server.quit()
