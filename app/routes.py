from server import app

@app.route('/main')
def main():
    return 'Hello world!'