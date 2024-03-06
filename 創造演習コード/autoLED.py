import RPi.GPIO as GPIO
import time

LIGHT_INPUT = 0
LED_OUTPUT = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(LIGHT_INPUT,GPIO.IN)
GPIO.setup(LED_OUTPUT,GPIO.OUT)

while True:
    if GPIO.input(LIGHT_INPUT) == GPIO.HIGH:
        GPIO.output(LED_OUTPUT,GPIO.HIGH)
    else:
        GPIO.output(LED_OUTPUT,GPIO.LOW)
    print(GPIO.input(LIGHT_INPUT))
    time.sleep(1)
