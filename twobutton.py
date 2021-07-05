# 兩個按鍵
import RPi.GPIO as GPIO
import time

n1 = 1
n2 = 1
def event_occurred(pin):
    global n1,n2
    if (pin ==pinBN1):
        print('pressed{} key {} '.format(pin,n1)
        n1 += 1
    elif (pin ==pinBN2):
        print('pressed{} key{} '.format(pin,n2)
        n2 += 1
pinBN1 = 4
pinBN2 = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBN1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinBN2,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(pinBN1,GPIO.FALLING,callback=event_occurred)
GPIO.add_event_detect(pinBN2,GPIO.RISING,callback=event_occurred)

try:
    while True:
              time.sleep(100000)
except:
    pass




    

