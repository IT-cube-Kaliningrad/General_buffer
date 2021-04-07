from server import app

@app.route('/')
@app.route('/main')
def main():
    return 'Hello world!'