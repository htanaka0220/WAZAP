# coding: utf-8
import FaBoAmbientLight_ISL29034
import time
import sys
import RPi.GPIO as g

ISL29034 = FaBoAmbientLight_ISL29034.ISL29034()

LED_PIN_NUM = 18
g.setmode(g.BCM)
g.setup(LED_PIN_NUM,g.OUT)

try:
    while True:

        lux  = ISL29034.read()

        sys.stdout.write("\rLux=%f" % lux)
        if lux <= 80:
            g.output(LED_PIN_NUM,True)
        else:
            g.output(LED_PIN_NUM,False)
            
        sys.stdout.flush()


        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
