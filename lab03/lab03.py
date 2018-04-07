#!/usr/bin/python

'''
Lab 03

In this lab you will connect to MediaTek LinkIt Smart a button 
and send button's data to the cloud backend - dweet.io and see
this data at the freeboard.io.

Button should be connected as following

Actuator      -->      LinkIt Smart
-----------------------------------
VCC (Red)     -->      3V3
SIG (Yellow)  -->      P31
GND (Black)   -->      GND

Logic of work:
1. Start script and show welcome prompt
2. Go to supercycle
3. Scan button
4. If button is pressed then log to the console and send data to the cloud backend

For exit from script please press Ctrl+C

'''

# Import dependencies 
import mraa
import requests

# Select and configure GPIO pin for SIG pin
pinSIG = mraa.Gpio(14)
pinSIG.dir(mraa.DIR_IN)

# Button state variable
stateButton = False

# Address variable
# Give name to your device
# FIX DEVICE NAME
yourDevice = 'YOUR_DEVICE_AMAZING_NAME'

# Welcome prompt
print("The script starts now.")

# Endless cycle
while True:
    try:
        if (pinSIG.read() == 1 and stateButton == False):
            stateButton = True
            r = requests.get('https://dweet.io/dweet/for/' + yourDevice + '?state=True')
            print("Button Pressed!")
        if (pinSIG.read() == 0 and stateButton == True):
            stateButton = False
            r = requests.get('https://dweet.io/dweet/for/' + yourDevice + '?state=False')
            # Add output to the console
            # WRITE YOUR CODE HERE


    except KeyboardInterrupt:
        print("The script ends now.")