. venv/bin/activate
# Переменные окружения
#   FLASK
    export FLASK_APP=server/server.py
    export FLASK_ENV=development
    export FLASK_DEBUG=0
#   SERVER
    export SERVER_HOST=127.0.0.1
    export SERVER_PORT=5000

flask run --host $SERVER_HOST --port $SERVER_PORT