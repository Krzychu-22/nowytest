from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Testing monitorrrrrr"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
