# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 12:10:17 2014

@author: Camilo B.
"""

from matplotlib.colors import LogNorm
from pylab import *
import random
import numpy as np
from matplotlib.widgets import Slider, Button, RadioButtons
import serial 
import matplotlib.pyplot as plt
from drawnow import *



arduinoSerialData = serial.Serial('com3',9600) #Create Serial port object called arduinoSerialData

plt.ion()

p = 0
x = 0
y = 0
 
def makeFig():
    plt.subplot()
    plt.hist2d(x, y, bins=50,range=np.array([(-5, 5), (-5, 5)]))
    colorbar()

while True:
    while (arduinoSerialData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    
    myData = arduinoSerialData.readline()
    p = float(myData)
    SampleSize =22.67*math.exp(0.21*p) 
    
    x = randn(SampleSize)
    y = randn(SampleSize)
    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.00000001)                     #Pause Briefly. Important to keep drawnow from crashing