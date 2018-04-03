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
    # LED/Buzzer ON
    pinSIG.write(1)
    # Wait for 1 second
    time.sleep(1)
    # LED/Buzzer OFF
    pinSIG.write(0)
    # Wait for 1 second again
    time.sleep(1)