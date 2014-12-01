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
time.sleep(1.5)


p = 0
x = randn(1)
y = randn(1)
plt.hist2d(x, y, bins=50,range=np.array([(-6, 6), (-6, 6)]))
plt.colorbar()

i = 0
t = 0
def makeFig():
    #plt.hist(x, bins = 100) 
    #xlim([-5, 5])
    #ylim([0, 80])
    ##plt.colorbar()
    #plt.pause(.000000000001) 
    hist2d(x, y, bins=50,range=np.array([(-5, 5), (-5, 5)]))
    colorbar()
    ##plt.hexbin(x, y,gridsize=30, cmap=CM.jet, bins=None)
    ##plt.axis([x.min(), x.max(), y.min(), y.max()])
    
    

while True:
    while (arduinoSerialData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    
    myData = arduinoSerialData.readline()
    i = i + 1
    p = float(myData)*4
    if(p<40):
        SampleSize =18*math.exp(0.2*p) 
    else:
        SampleSize =18*math.exp(0.2*40)    
    
    ##x = np.random.uniform(-p/15, p/15, size=SampleSize)
    
    ##y = np.random.uniform(-p/20, p/20, size=SampleSize)
    x = randn(SampleSize-17)
    y = randn(SampleSize-17)
    #drawnow(makeFig)      
    print p
    ##print SampleSize
    ##plt.subplot()
    ##plt.hist2d(x, y, bins=50,range=np.array([(-5, 5), (-5, 5)]))
    plt.ion()
    if(i%6==0):
        drawnow(makeFig)
        plt.pause(.000000000001) 
        print t
        t= t+1
    ##plt.hist2d(x, y, bins=50,range=np.array([(-5, 5), (-5, 5)]))
    ##plt.hexbin(x, y,gridsize=30, cmap=CM.jet, bins=None)    
    ##plt.pause(.000000000001)                     #Pause Briefly. Important to keep drawnow from crashing
    ##time.sleep(0.5)