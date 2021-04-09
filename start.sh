# Переменные окружения
#   FLASK
    export FLASK_APP=server/server.py
    export FLASK_ENV=development
    export FLASK_DEBUG=1
#   SERVER
    export SERVER_HOST=192.168.137.77
    export FLASK_RUN_PORT=5000

# Запуск
flask run --host $SERVER_HOST