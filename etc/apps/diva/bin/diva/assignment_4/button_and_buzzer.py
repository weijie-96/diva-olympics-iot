import time
import grovepi
import math

buzzer_pin = 2      #Port for buzzer
button = 4      #Port for Button

grovepi.pinMode(buzzer_pin,"OUTPUT")    # Assign mode for buzzer as output
grovepi.pinMode(button,"INPUT")     # Assign mode for Button as input
while True:
    try:
        button_status= grovepi.digitalRead(button)  #Read the Button status
        if button_status:   #If the Button is in HIGH position, run the program
            grovepi.digitalWrite(buzzer_pin,1)                      
            # print "\tBuzzing"         
        else:       #If Button is in Off position, print "Off" on the screen
            grovepi.digitalWrite(buzzer_pin,0)
            # print "Off"           
    except KeyboardInterrupt:   # Stop the buzzer before stopping
        grovepi.digitalWrite(buzzer_pin,0)
        break
    except (IOError,TypeError) as e:
        print("Error")