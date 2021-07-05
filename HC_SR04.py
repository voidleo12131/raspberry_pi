# 超音波感測器（1）

import RPi.GPIO as GPIO
import time

pinECHO = 14
pinTRIG = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinECHO, GPIO.IN)
GPIO.setup(pinTRIG, GPIO.OUT)

def pulseIn(pin):
    if GPIO.wait_for_edge(pin,GPIO.RISING,timeout=500) is None:
        return 0
    start_time = time.time()
    GPIO.wait_for_edge(pin,GPIO.FALLING,timeout=500)
    return (time.time()-start_time) * 1000000
try:
    while True:
        GPIO.output(pinTRIG, 0)
        time.sleep(2 / 1000000)

        GPIO.output(pinTRIG, 1)
        time.sleep(10 / 1000000)
        GPIO.output(pinTRIG, 0)

        d = pulseIn(pinECHO) / 28.9 / 2
        if d > 400 or d == 0:
            continue
        print ("Distance: " + str(d) + " cm")
        time.sleep(0.5)

except:
    pass

GPIO.cleanup()

