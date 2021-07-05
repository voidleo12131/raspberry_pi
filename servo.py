# 舵機
import RPi.GPIO as GPIO
import time

pin = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
p = GPIO.PWM(pin,50)
p.start(6)
time.sleep(1)
while True:
    p.ChangeDutyCycle(12)
    time.sleep(1)
    p.ChangeDutyCycle(7.5)
    time.sleep(1)
p.stop()
GPIO.cleanup()