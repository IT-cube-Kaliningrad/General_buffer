: Режим "Ни слова по-русски"
@echo off

: Запуск виртуального окружения
venv\Scripts\activate

: Переменные окружения
:   FLASK
    set FLASK_APP=server/server.py
    set FLASK_ENV=development
    set FLASK_DEBUG=0
:   SERVER
    set SERVER_HOST=127.0.0.1
    set FLASK_RUN_PORT=5000

: Запуск
flask run --host %SERVER_HOST%
deactivate