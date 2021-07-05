# 按鍵按壓次數
import RPi.GPIO as GPIO
import time
n = 1
def event_occurred(pin):
    global n
    print('press{} time'.format(n))
    n += 1

pinBN = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinBN,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(pinBN,GPIO.FALLING,callback=event_occurred)

try:
    while True:
        time.sleep(10000)
except:
    pass
finally:
    GPIO.cleanup()
