from flask import Flask, render_template
app = Flask(__name__)

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

@app.route('/')
def init():
    #Motor 1 Pin Layout
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)

    #Motor 2 Pin Layout
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(18, GPIO.OUT)

    # Turn off all pins (will redirect to here for stopping motion.)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)

    GPIO.output(16, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)

    return render_template("base.html")


@app.route('/forward')
def forward():
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)

    GPIO.output(16, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    return render_template("base.html")


@app.route('/backward')
def backward():
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)

    GPIO.output(18, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    return render_template("base.html")

@app.route('/left')
def left():
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(24, GPIO.LOW)

    GPIO.output(18, GPIO.HIGH)
    GPIO.output(16, GPIO.LOW)
    return render_template("base.html")

@app.route('/right')
def right():
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(22, GPIO.LOW)

    GPIO.output(16, GPIO.HIGH)
    GPIO.output(18, GPIO.LOW)
    return render_template("base.html")

GPIO.cleanup()

