import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
while True:
    print(GPIO.input(17))
    time.sleep(1)