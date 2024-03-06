import wiringpi as w
import time
w.wiringPiSetup()
w.pinMode(0, 0)
w.pinMode(1, 1)
 
while 1:
  switch = w.digitalRead(0)
  if 1 == switch:
    print(1)
    w.digitalWrite(1,1)
  else:
    print(0)
    w.digitalWrite(1,0)
  time.sleep(1)
