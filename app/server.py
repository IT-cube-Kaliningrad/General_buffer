from flask import Flask
from settings import SERVER_IP

app = Flask(__name__)

import routes

app.run(host=SERVER_IP)