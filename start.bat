@echo off
: Переменные окружения
:   FLASK
    set FLASK_APP=server/server.py
    set FLASK_ENV=development
    set FLASK_DEBUG=0
:   SERVER
    set SERVER_HOST=192.168.0.3
    set FLASK_RUN_PORT=5000

flask run --host %SERVER_HOST%