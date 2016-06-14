
#RPi.GPIO is a library of commands to easily control the Pi's GPIO pins
import RPi.GPIO as GPIO

#time is a common library used to create delays of specific length
import time

#set the pin designation type to GPIO.BCM to use BCM numbering convention
GPIO.setmode (GPIO.BCM)

#LED connected to GPIO 4
LIGHT = 4

#GPIO pins ac as either digital inputs or outputs. need to tell Pi to switch to GPIO.BOARD  if rather use the pyhsical pin number
GPIO.setup(LIGHT, GPIO.OUT)

#blinking the LED by toggling the state true(send high signal) and false(LOW)
while True:
	GPIO.output(LIGHT, True)
	time.sleep(0.5)
	GPIO.output(LIGHT, False)
	time.sleep(0.5)

