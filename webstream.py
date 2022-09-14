from flask import Response
from flask import Flask
from flask import render_template
from flask import jsonify
import threading
import datetime
import time
import serial
import random

output = 0
lock = threading.Lock()

app = Flask(__name__)

ser=serial.Serial(port='/dev/ttyS2',
baudrate=9600,
timeout=1)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/live_signal')
def live_signal():
    global output, lock
    with lock:
        return jsonify(final_signal = output)

def gen():
	while True:
		x=ser.readline()
		x=str(x, 'utf-8')
		return x

def run_signal():
    global output, lock
    while True:
        temp = gen()
        with lock:
            output = temp


if __name__ == '__main__':
    t = threading.Thread(target = run_signal)
    t.daemon = True
    t.start()
    app.run(host='0.0.0.0', port=80, debug=True, threaded=True, use_reloader=False)
