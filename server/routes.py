from server import app
from flask import render_template, request

data = None

@app.route('/', methods=('GET', 'POST'))
def main():
    global data
    if request.method == 'POST':
        data = request.json['data']
    return render_template('main.html', data=data)