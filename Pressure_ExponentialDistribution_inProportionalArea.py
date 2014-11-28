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
from matplotlib import cm as CM



arduinoSerialData = serial.Serial('com3',115200) #Create Serial port object called arduinoSerialData



p = 0
x = randn(1)
y = randn(1)
plt.hist2d(x, y, bins=50,range=np.array([(-6, 6), (-6, 6)]))
colorbar()

def makeFig():
    hist2d(x, y, bins=50,range=np.array([(-5, 5), (-5, 5)]))
    ##colorbar()
    ##plt.hexbin(x, y,gridsize=30, cmap=CM.jet, bins=None)
    ##plt.axis([x.min(), x.max(), y.min(), y.max()])
    

while True:
    while (arduinoSerialData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    
    myData = arduinoSerialData.readline()
    p = float(myData)*4
    if(p<40):
        SampleSize =10*math.exp(0.21*p) 
    else:
        SampleSize =10*math.exp(0.21*40)    
    
    ##x = np.random.uniform(-p/15, p/15, size=SampleSize)
    
    ##y = np.random.uniform(-p/20, p/20, size=SampleSize)
    x = randn(SampleSize-9)
    y = randn(SampleSize-9)
    drawnow(makeFig)      
    print p
    ##print SampleSize
    ##plt.subplot()
    ##plt.hist2d(x, y, bins=50,range=np.array([(-5, 5), (-5, 5)]))
    plt.ion()
    ##plt.hist2d(x, y, bins=50,range=np.array([(-5, 5), (-5, 5)]))
    ##plt.hexbin(x, y,gridsize=30, cmap=CM.jet, bins=None)    
    plt.pause(.000000000001)                     #Pause Briefly. Important to keep drawnow from crashing
    ##time.sleep(0.05)