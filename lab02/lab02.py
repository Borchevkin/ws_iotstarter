#!/usr/bin/python

'''
Lab 02

In this lab you will connect to MediaTek LinkIt Smart a simple sensor - button.

Button should be connected as following

Actuator      -->      LinkIt Smart
-----------------------------------
VCC (Red)     -->      3V3
SIG (Yellow)  -->      P31
GND (Black)   -->      GND

Logic of work:
1. Start script and show welcome prompt
2. Go to supercycle
3. Scan button.
4. If button is pressed then log in the console

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

# Welcome prompt
print("The script starts now.")

# Endless cycle
while True:
    if (pinSIG.read() == 1 and stateButton == False):
        stateButton = True
        print("Button Pressed!")
    if (pinSIG.read() == 0 and stateButton == True):
        stateButton = False
        print("Button Depressed!")