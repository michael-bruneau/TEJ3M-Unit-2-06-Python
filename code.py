# Created by: Michael Bruneau
# Created on: March 2025
#
# This module is a Raspberrypy Pico program causes micro Servo to to turn back and forth from 180 degress to 0 degrees


import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)


# variables
seconds_to_microseconds_conversion_number = 
sonar_delay = 2 / seconds_to_microseconds_conversion_number

# setup
led = digitalio.DigitalInOut(board.GP12)
led.direction = digitalio.Direction.OUTPUT

# loop
while True:
    print(f"Distance: {sonar.distance} cm")

