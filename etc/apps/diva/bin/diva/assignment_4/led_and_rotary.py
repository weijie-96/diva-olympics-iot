import time
import grovepi

# Connect the Grove LED to digital port D5
led = 5

# Connect the Grove Rotary Angle Sensor to analog port A0
potentiometer = 0


grovepi.pinMode(potentiometer,"INPUT")
grovepi.pinMode(led,"OUTPUT")

time.sleep(1)
i = 0

while True:
    try:
        # Read resistance from Rotary Angle Sensor
        i = grovepi.analogRead(potentiometer)
        print (i)

        # Give PWM output to LED
        grovepi.analogWrite(led,i/4)

    except IOError:
        print ("Error")