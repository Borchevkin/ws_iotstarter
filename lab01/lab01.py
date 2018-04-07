#!/usr/bin/python

'''
Lab 01

In this lab you will connect to MediaTek LinkIt Smart a simple actuators - led and buzzer.

Actuator should be connected as following

Actuator      -->      LinkIt Smart
-----------------------------------
VCC (Red)     -->      3V3
SIG (Yellow)  -->      P31
GND (Black)   -->      GND

Logic of work:
1. Start script and show welcome prompt
2. Go to supercycle
3. Blink/buzz every 1 second

For exit from script please press Ctrl+C

'''

# Import dependencies 
import mraa
import time
import requests

# Select and configure GPIO pin for SIG pin
pinSIG = mraa.Gpio(14)
pinSIG.dir(mraa.DIR_OUT)

# Welcome prompt
print("The script starts now.")

# Endless cycle
while True:
    try:
        # LED/Buzzer ON. For it please use write(LEVEL) method of pinSIG
        # WRITE YOUR CODE HERE
        
        # Wait for 1 second. Please use time.sleep method
        # WRITE YOUR CODE HERE

        # And now please think what you need to write for blinking/buzzing
        # WRITE YOUR CODE HERE

    except KeyboardInterrupt:
        print("The script ends now.")