#! /usr/bin/env python
from flask import Flask, render_template, request
#app = Flask(__name__,template_folder='.',static_folder='.',static_url_path='/.')
app = Flask(__name__,template_folder='.')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
		print 'Do something'
		return render_template('index.php')
    elif request.method == 'GET':
		print 'Do something'
		return render_template('index.php')

@app.route('/start.php')
def start():
    return send_from_directory(app.static_folder, request.path[1:])

if __name__ == '__main__':
   app.run(debug = True)
