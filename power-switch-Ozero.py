#!/usr/bin/env python3
import OPi.GPIO as GPIO # to install "pip3 install --upgrade OPi.GPIO"
import time
import subprocess
GPIO.setmode(GPIO.BOARD)

#Select unused GPIO header pin to be used for shutdown
InputPin = 12 

# Set selected pin to input, need pullup resistor external in 3.3V and pin select.
GPIO.setup(InputPin, GPIO.IN)

if GPIO.input(InputPin):
    print('Input was HIGH')
else:
    print('Input was LOW')

# Wait for a button press on the selected pin (pin pulled to ground, falling edge)
GPIO.wait_for_edge(InputPin, GPIO.FALLING)

print ("*** Netctl shutdown activated ***")
subprocess.call("/sbin/shutdown now", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)