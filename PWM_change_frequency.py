#  更改亮燈頻率
import RPi.GPIO as GPIO
import time

pinLED = 21
freq = 0.5
dc = 0.5
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinLED,GPIO.OUT)
p = GPIO.PWM(pinLED,freq)

p.start(dc)
input('enter to stop')
p.ChangeFrequency(1)
p.ChangeDutyCycle(90)
input('enter to stop')
p.stop()

GPIO.cleanup()
