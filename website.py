#! /usr/bin/env python
import os
from flask import Flask, render_template, request
app = Flask(__name__,template_folder='.')

directory = os.path.dirname(os.path.realpath(__file__))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
		for item in request.form:
			if item == 'start':
				print 'start stream'
				os.system(directory+'/start-stream')
			if item == 'stop':
				print 'stop stream'
				os.system(directory+'/stop-stream')
		return render_template('index.php')
    elif request.method == 'GET':
		return render_template('index.php')

if __name__ == '__main__':
   app.run()
