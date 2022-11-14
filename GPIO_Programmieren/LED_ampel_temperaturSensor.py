import time
import board
import adafruit_bmp280
import RPi.GPIO as GPIO


def setup():
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(17,GPIO.OUT)
        GPIO.setup(22,GPIO.OUT)
        GPIO.setup(27,GPIO.OUT)
        GPIO.output(17, False)
        GPIO.output(22, False)
        GPIO.output(27, False)
# Sensorobjekt erstellen, das ueber den Standard-I2C-Bus des RPi kommuniziert
i2c = board.I2C()   # benutzt board.SCL und board.SDA
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Aendern Sie diesen Wert so, dass er dem Luftdruck (hPa) auf Meereshoehe an ihrem Standort entspricht.
bmp280.sea_level_pressure = 1013.25
setup()
while True:
    if bmp280.temperature > 30 and bmp280.temperature < 31:
        GPIO.output(17, False)
        GPIO.output(22, False)
        GPIO.output(27, True)
    elif bmp280.temperature > 31:
        GPIO.output(17, False)
        GPIO.output(22, True)
        GPIO.output(27, False)
    else:
        GPIO.output(17, True)
        GPIO.output(22, False)
        GPIO.output(27, False)
