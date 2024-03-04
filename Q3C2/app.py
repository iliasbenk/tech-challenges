from flask import Flask, jsonify, make_response
import psycopg2

app = Flask(__name__)


def connect_db():
    try:
        conn = psycopg2.connect(
            host="db",
            database="postgres",
            user="postgres",
            password="postgres",
            connect_timeout=5)
        cur = conn.cursor()
        cur.execute('SELECT 1')
        return cur.fetchone()[0]
    except (psycopg2.OperationalError, psycopg2.DatabaseError):
        return None


@app.route('/')
def hello_world():
    return f'Hello, World!'


@app.route('/health')
def health():
    msg = 'Success' if connect_db() is not None else 'DB down!'
    if msg == 'Success':
        return make_response(jsonify({'message': msg}), 200)
    else:
        return make_response(jsonify({'message': msg}), 500)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
