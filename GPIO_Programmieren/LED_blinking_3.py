import RPi.GPIO as GPIO
import time

state = False

def setup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4,GPIO.OUT)
        GPIO.setup(3,GPIO.OUT)
        GPIO.setup(2,GPIO.OUT)
        GPIO.output(4, False)
        GPIO.output(3, False)
        GPIO.output(2, False)

def turnAmpelOn():
    GPIO.output(2, False)
    GPIO.output(3, True)
    time.sleep(1)
    GPIO.output(3, False)
    GPIO.output(4, True)

def turnAmpelOff():
    GPIO.output(4, False)
    GPIO.output(3, True)
    time.sleep(1)
    GPIO.output(3, False)
    GPIO.output(2, True)

def changeState():
    global state
    print(state)
    if state == True:
        state = False
        print("turn on")
        turnAmpelOn()
    else:
        print("turn off")
        state = True
        turnAmpelOff()

setup()
changeState()
while True:
    varInput = input("click enter to change ampel")
    if varInput == '':
        changeState()
