# Created by: Michael Bruneau
# Created on: March 2025
#
# This module is a Raspberrypy Pico program displays distance from sonar and truns on LED if an object gets to close to the sonar


import time
import board
import adafruit_hcsr04
import digitalio


# variables
seconds_to_microseconds_conversion_number = 1000000
sonar_delays = [2 / seconds_to_microseconds_conversion_number, 10 / seconds_to_microseconds_conversion_number]
delay_between_sonar_cheeks = 10
distance = 0
too_close = 20

# setup
led = digitalio.DigitalInOut(board.GP12)
led.direction = digitalio.Direction.OUTPUT
sonar = adafruit_hcsr04.HCSR04(trigger_pin = board.GP15, echo_pin = board.GP14)

# loop
while True:
    # Sonar gets the distance form object
    time.sleep(sonar_delays[0])
    distance = sonar.distance
    time.sleep(sonar_delays[1])

    print(f"Distance: {distance} cm")

    # turns on LED  an object distance is equal to or closer then 20 cm from the sonar make 20 a cosntant and comment on  the working timer
    if distance <= too_close0:
        led.value = True
    else:
        led.value = False

    # The commented out code is not apart of the actual code but is needed to get it working by uncomenting it and recomenting it
    #time.sleep(delay_between_sonar_cheeks)
