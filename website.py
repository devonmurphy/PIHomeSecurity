#! /usr/bin/env python
import os
from flask import Flask, render_template, request
app = Flask(__name__,template_folder='.')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
		for item in request.form:
			if item == 'start':
				print 'start stream'
				os.system('./start-stream')
			if item == 'stop':
				print 'stop stream'
		return render_template('index.php')
    elif request.method == 'GET':
		return render_template('index.php')

if __name__ == '__main__':
   app.run(debug = True)
