# 超音波感測器（2）
import RPi.GPIO as GPIO
import time

pinECHO = 14
pinTRIG = 15
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinECHO, GPIO.IN)
GPIO.setup(pinTRIG, GPIO.OUT)

def getDistance():
    GPIO.output(pinTRIG,1)
    time.sleep(0.000001)
    GPIO.output(pinTRIG,0)
    
    if GPIO.wait_for_edge(pinECHO,GPIO.RISING,timeout=500) is None:
        return 0
    pulseStart = time.time()
    GPIO.wait_for_edge(pinECHO,GPIO.FALLING,timeout=500)
    pulseStop = time.time()
    distance = (pulseStop - pulseStart)*34600/2
    return distance
try:
    while True:
        distance = getDistance()
        print('Distance{} cm'.format(distance))
        time.sleep(1)
except:
    pass
GPIO.cleanup()