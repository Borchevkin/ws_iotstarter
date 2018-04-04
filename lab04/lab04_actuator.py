#!/usr/bin/python

'''
Lab 04 - actuator

In this lab you will connect to MediaTek LinkIt Smart a simple actuators - led and buzzer 
and change the state of the actuator depending on the data on the cloud backend - dweet.io.

Button should be connected as following

Actuator      -->      LinkIt Smart
-----------------------------------
VCC (Red)     -->      3V3
SIG (Yellow)  -->      P31
GND (Black)   -->      GND

Logic of work:
1. Start script and show welcome prompt
2. Go to supercycle
3. Scan data on the cloud backend
4. If button "state" is "True" then log to the console and set actuator ON

For exit from script please press Ctrl+C

'''

# Import dependencies 
import mraa
import requests

# Select and configure GPIO pin for SIG pin
pinSIG = mraa.Gpio(14)
pinSIG.dir(mraa.DIR_OUT)

# Address variable
yourDevice = 'linkit_button_test'

# Welcome prompt
print("The script starts now.")

# Endless cycle
while True:
    try:
        checkState = requests.get('https://dweet.io/get/latest/dweet/for/' + yourDevice)
        if ("True" in checkState.text):
            pinSIG.write(1)
            print("Actuator is ON")
        if ("False" in checkState.text):
            pinSIG.write(0)
            print("Actuator is OFF")
    except KeyboardInterrupt:
        print("The script ends now.")