# 兩個ＬＥＤ兩的按鍵
import RPi.GPIO as GPIO
import time
pinLED = 21
pinled = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED,GPIO.OUT)
GPIO.setup(pinled,GPIO.OUT)
GPIO.output(pinLED,0)
GPIO.output(pinled,0)

try:
    while True:
        GPIO.output(pinLED,1)
        time.sleep(0.2)
        GPIO.output(pinLED,0)
        time.sleep(0.2)
        GPIO.output(pinled,1)
        time.sleep(0.1)
        GPIO.output(pinled,0)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
GPIO.cleanup()

