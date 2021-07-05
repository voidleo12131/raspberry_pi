import time ,smbus
import RPi.GPIO as GPIO

pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
p = GPIO.PWM(pin,50)

i2c = smbus.SMBus(1)

addr = 0x53

i2c.write_byte_data(addr, 0x2C , 0x0B)

i2c.write_byte_data(addr ,0x2D, 0x08)

i2c.write_byte_data(addr ,0x31 ,0x08 | 0x02)

def axesData(reg):
	bytes =i2c.read_i2c_block_data(addr ,reg ,2)
	axes = bytes[0] |(bytes[1]<< 8)
	if (axes & (1 <<16 -1)):
		axes = axes-(1<<16)
	return round(axes/256 , 2)

while True:
	x =axesData(0x32)
	y =axesData(0x34)
	z =axesData(0x36)
	ang = (x+1)*90
	print("ang={:.1f}".format(ang))
	degree = ang/9.5+2.5
	p.start(degree)
	p.ChangeDutyCycle(degree)
	#print('x={}\ty={}\tz={}'.format(x,y,z))
	time.sleep(0.2
)
	
