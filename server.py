from flask import Flask
from settings import*
import os

#Инициализация Flask
app = Flask(__name__)
app.run
#Установка переменных окружения для flask
os.environ['FLASK_ENV'] = FLASK_ENV
os.environ['FLASK_DEBUG'] = str(FLASK_DEBUG)
os.environ['FLASK_APP'] = FLASK_APP
#Запуск сервера
os.system(f'flask run --host {SERVER_HOST} --port {SERVER_PORT}')