# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 11:50:56 2014

@author: Camilo
"""

import serial #Import Serial Library
 
arduinoSerialData = serial.Serial('com3',9600) #Create Serial port object called arduinoSerialData
 
 
while (1==1):
      if(arduinoSerialData.inWaiting()>0): 
        myData = arduinoSerialData.readline()
        print float(myData)
