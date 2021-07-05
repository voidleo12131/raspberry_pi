import RPi.GPIO as GPIO
import time

pinDS = 21
pinSTCP = 20
pinSHCP = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup([pinDS, pinSTCP, pinSHCP], GPIO.OUT)

data = [[1, 1, 1, 1, 1, 1, 0, 1], #0
        [0, 1, 1, 0, 0, 0, 0, 1], #1
        [1, 1, 0, 1, 1, 0, 1, 1], #2
        [1, 1, 1, 1, 0, 0, 1, 1], #3
        [0, 1, 1, 0, 0, 1, 1, 1], #4
        [1, 0, 1, 1, 0, 1, 1, 1], #5
        [0, 0, 1, 1, 1, 1, 1, 1], #6
        [1, 1, 1, 0, 0, 0, 0, 1], #7
        [1, 1, 1, 1, 1, 1, 1, 1], #8
        [1, 1, 1, 0, 0, 1, 1, 1], #9
        [0, 0, 0, 0, 0, 0, 0, 0], #off
        [1, 1, 1, 0, 1, 1, 1, 0], #A
        [1, 1, 1, 1, 1, 1, 1, 0], #B
        [1, 0, 0, 1, 1, 1, 0, 0], #C
        [1, 1, 1, 1, 1, 1, 0, 0]] #D
try:
	for i in range(len(data)):
		GPIO.output(pinSTCP, 0)
		for j in range(8):
			GPIO.output(pinSHCP, 0)
			GPIO.output(pinDS, data[i][j])
			GPIO.output(pinSHCP, 1)
		GPIO.output(pinSTCP, 1)
		time.sleep(0.5) # 間隔0.5秒
except KeyboardInterrupt:
	pass
time.sleep(2)
GPIO.cleanup()
