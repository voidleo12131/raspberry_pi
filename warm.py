# 溫濕度感測器
import dht11 
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

sensor = dht11.DHT11(pin=21)


while True:
    result = sensor.read()
    if result.is_valid():
        print ('temperature:{:.1f}C,Humidity:{:.0f}%'.format(result.temperature,result.humidity))
        time.sleep(5) 