from server import app
from flask import render_template, request

data = 'NULL'

@app.route('/data', methods=('GET', 'POST'))
def return_data():
    global data
    if request.method == 'POST':
        data = request.json['data']
    return data

@app.route('/')
def main():
    global data
    return render_template('main.html', data=data)