#!/usr/bin/python

'''
Lab 04 - sensor

In this lab you will connect to MediaTek LinkIt Smart a button 
and send button's data to the cloud backend - dweet.io.

Button should be connected as following

Actuator      -->      LinkIt Smart
-----------------------------------
VCC (Red)     -->      
SIG (Yellow)  -->   
GND (Black)   -->

Logic of work:
1. Start script and show welcome prompt
2. Go to supercycle
3. Scan button
4. If button is pressed then log to the console and send data to the cloud backend

For exit from script please press Ctrl+C

'''

while(1):