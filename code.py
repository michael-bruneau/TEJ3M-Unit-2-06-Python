# Created by: Michael Bruneau
# Created on: March 2025
#
# This module is a Raspberrypy Pico program causes micro Servo to to turn back and forth from 180 degress to 0 degrees


import time
import board
import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)


# variables
seconds_to_microseconds_conversion_number = 1000000
sonar_delays = [2 / seconds_to_microseconds_conversion_number, 10 / seconds_to_microseconds_conversion_number]
distance = null

# setup
led = digitalio.DigitalInOut(board.GP12)
led.direction = digitalio.Direction.OUTPUT

# loop
while True:
    # Sonar gets the disatnec form object
    sonar_delays[0]
    distance = sonar.distance
    sonar_delays[1]

    print(f"Distance: {distance} cm")

    # turns on LED  an object distance is equal to or closer then 20 cm from the sonar
    if distance <= 20:
        led.value(True)
    else:
        led.value(False)
