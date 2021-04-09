# Переменные окружения
#   FLASK
    export FLASK_APP=server/server.py
    export FLASK_ENV=production
    export FLASK_DEBUG=0
#   SERVER
    export SERVER_HOST=127.0.0.1
    export FLASK_RUN_PORT=5000

# Запуск
flask run --host $SERVER_HOST