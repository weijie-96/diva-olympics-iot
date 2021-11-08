import grovepi

# Connect the Grove Ultrasonic Ranger to digital port D4
ultrasonic_ranger = 4

# Connect Buzzer to digital port D2
buzzer = 2

grovepi.pinMode(buzzer,"OUTPUT")

while True:
    try:
        # Read distance value from Ultrasonic
        distant = grovepi.ultrasonicRead(ultrasonic_ranger)
        print(distant,'cm')
        if distant <= 10:
            grovepi.digitalWrite(buzzer,1)
        else:
            grovepi.digitalWrite(buzzer,0)

    except TypeError:
        print("Error")
    except IOError:
        print("Error")