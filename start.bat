: Режим "Ни слова по-русски"
@echo off
: Переменные окружения
:   FLASK
    set FLASK_APP=server/server.py
    set FLASK_ENV=development
    set FLASK_DEBUG=1
:   SERVER
    set SERVER_HOST=192.168.1.111
    set FLASK_RUN_PORT=5000

: Запуск
flask run --host %SERVER_HOST%