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



arduinoSerialData = serial.Serial('COM4',115200) #Create Serial port object called arduinoSerialData
time.sleep(1.5)


p = 0
x = randn(1)
y = randn(1)
#3plt.hist2d(x, y, bins=50,range=np.array([(-6, 6), (-6, 6)]))
plt.hist2d(x, y, bins=75,range=np.array([(-6, 6), (-6, 6)]))
plt.colorbar()


i = 0
t = 0
def makeFig():
    #plt.hist(x, bins = 100) 
    #xlim([-5, 5])
    #ylim([0, 80])
    ##plt.colorbar()
    #plt.pause(.000000000001) 
    ##plt.subplot()
    plt.hist2d(x1, y1, bins=75,range=np.array([(-6, 6), (-6, 6)]))
    ##plt.subplot()
    ##hist2d(x2, y2, bins=50,range=np.array([(-6, 6), (-6, 6)]))
    colorbar()
    
    
    

while True:
    while (arduinoSerialData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    
    myData = arduinoSerialData.readline()
    i = i + 1
    pv = float(myData)
    p= pv*5
    
    if(p<45):
        SampleSize =18*math.exp(0.2*p) 
    else:
        SampleSize =18*math.exp(0.2*45)    
    
    ##x = np.random.uniform(-p/15, p/15, size=SampleSize)
    
    ##y = np.random.uniform(-p/20, p/20, size=SampleSize)
    x1 = randn(SampleSize-17)
    y1 = randn(SampleSize-17)
    
    
    
    #drawnow(makeFig)      
    print pv
    ##print SampleSize
    ##plt.subplot()
    ##plt.hist2d(x, y, bins=50,range=np.array([(-5, 5), (-5, 5)]))
    plt.ion()
    if(i%4==0):
        drawnow(makeFig)
        ##plt.subplot()
        ##plt.hist2d(x, y, bins=50,range=np.array([(-5, 5), (-5, 5)]))
        ##plt.colorbar()
        plt.pause(.000000000001) 
        
    ##plt.hist2d(x, y, bins=50,range=np.array([(-5, 5), (-5, 5)]))
    ##plt.hexbin(x, y,gridsize=30, cmap=CM.jet, bins=None)    
    ##plt.pause(.000000000001)                     #Pause Briefly. Important to keep drawnow from crashing
    ##time.sleep(0.5)