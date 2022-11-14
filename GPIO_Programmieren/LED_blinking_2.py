import RPi.GPIO as GPIO
import time

def setup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4,GPIO.OUT)
def changeState(state):
    if state == "a":
        GPIO.output(4, False)
    elif state == "e":
        GPIO.output(4, True)

setup()
while True:
    state = input()
    changeState(state)