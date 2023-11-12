from flask import Flask
import os

app = Flask(__name__)


@app.route('/')
def hello():
    try:
        hostname = os.uname().nodename
    except AttributeError:
        hostname = ""
    return f"Hello, Docker Swarm! (Served by {hostname})\n"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
