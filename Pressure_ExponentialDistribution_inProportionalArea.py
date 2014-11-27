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
import time as time



arduinoSerialData = serial.Serial('com3',115200) #Create Serial port object called arduinoSerialData

ion()

p = 0
x = randn(1)
y = randn(1)
##plt.hist2d(x, y, bins=50,range=np.array([(-5, 5), (-5, 5)]))
##colorbar()

def makeFig():
    hist2d(x, y, bins=50,range=np.array([(-5, 5), (-5, 5)]))
    colorbar()
    

while True:
    ##while (arduinoSerialData.inWaiting()==0): #Wait here until there is data
      ##  pass #do nothing
    
    myData = arduinoSerialData.readline()
    p = float(myData)*4
    if(p<45):
        SampleSize =22.67*math.exp(0.21*p) 
    else:
        SampleSize =22.67*math.exp(0.21*42)    
    
    x = randn(SampleSize-21)
    y = randn(SampleSize-21)
    drawnow(makeFig)      
    ##print p                 #Call drawnow to update our live graph
    plt.pause(.00000000001)                     #Pause Briefly. Important to keep drawnow from crashing
    ##time.sleep(0.05)