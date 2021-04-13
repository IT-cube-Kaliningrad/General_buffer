from server import app
from flask import render_template, request

data = 'NULL'

@app.route('/', methods=('GET', 'POST'))
def main():
    global data
    if request.method == 'POST':
        data = request.json['data']
    return data