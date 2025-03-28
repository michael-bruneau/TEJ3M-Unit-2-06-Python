# Created by: Michael Bruneau
# Created on: March 2025
#
# This module is a Raspberrypy Pico program causes micro Servo to to turn back and forth from 180 degress to 0 degrees


import time
import board
import adafruit_hcsr04
import digitalio


# variables
seconds_to_microseconds_conversion_number = 1000000
sonar_delays = [2 / seconds_to_microseconds_conversion_number, 10 / seconds_to_microseconds_conversion_number]
delay_between_sonar_cheeks = 10
distance = 0

# setup
led = digitalio.DigitalInOut(board.GP12)
led.direction = digitalio.Direction.OUTPUT
sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.GP15, echo_pin = board.GP14)

# loop
while True:
    # Sonar gets the disatance form object
    time.sleep(sonar_delays[0])
    distance = sonar.distance
    time.sleep(sonar_delays[1])

    print(f"Distance: {distance} cm")

    # turns on LED  an object distance is equal to or closer then 20 cm from the sonar
    if distance <= 20:
        led.value = True
    else:
        led.value = False

    # This is to get it to work sorry
    time.sleep(delay_between_sonar_cheeks)
