from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Testing monitorrrrrr"

def run():
    app.run(host="0.0.0.0", port=7060)

def keep_alive():
    server = Thread(target=run)
    server.start()
