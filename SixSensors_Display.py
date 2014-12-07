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



arduinoSerialData = serial.Serial('com4',115200) #Create Serial port object called arduinoSerialData
time.sleep(2)


p = 0.0 # 0-40


SampleSize =22.67*math.exp(0.2855*p)

x = randn(SampleSize-21)
y = randn(SampleSize-21)
 

plt.hist2d(x, y, bins=150,range=np.array([(-25, 25), (-25, 25)]))
colorbar()


i = 0
t = 0

myData = range(6)

pv = range(6)
x = range(6)
y = range(6)
SampleSize = range(6)

def makeFig():
    plt.hist2d(x, y, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())  
    
    plt.hist2d(x1, y1, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
    plt.hist2d(x2, y2, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
    plt.hist2d(x3, y3, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
    plt.hist2d(x4, y4, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
    plt.hist2d(x5, y5, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
    #plt.hist(x, bins = 100) 
    #xlim([-5, 5])
    #ylim([0, 80])
    ##plt.colorbar()
    #plt.pause(.000000000001) 
    ##plt.subplot()
    #plt.hist2d(x1, y1, bins=75,range=np.array([(-6, 6), (-6, 6)]))
    ##plt.subplot()
    ##hist2d(x2, y2, bins=50,range=np.array([(-6, 6), (-6, 6)]))
    #colorbar()   
    




while True:
    while (arduinoSerialData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    
    arduinoString = arduinoSerialData.readline()
    dataArray = arduinoString.split(',')
    ##i = i + 1
    ##for i in range(0,6):
    print int(dataArray[0])
    print int(dataArray[1])
    print int(dataArray[2])
    print int(dataArray[3])
    print int(dataArray[4])
    print int(dataArray[5])    
    """
    pv[0] = int(dataArray[0])
    pv[1] = int(dataArray[1])
    pv[2] = int(dataArray[2])
    pv[3] = int(dataArray[3])
    pv[4] = int(dataArray[4])
    pv[5] = int(dataArray[5])
    
    
    for i in range(0,6):
        if(pv[i]<45):
            SampleSize[i] =30*math.exp(0.2*pv[i])
        else:
            SampleSize[i] =30*math.exp(0.2*pv[i])
    
    
    x = randn(SampleSize[0]-29)
    y = randn(SampleSize[0]-29)+15
    
    x1 = randn(SampleSize[1]-29)+7.5
    y1 = randn(SampleSize[1]-29)+12.99
    
    x2 = randn(SampleSize[2]-29)+12.99
    y2 = randn(SampleSize[2]-29)+7.5
    
    x3 = randn(SampleSize[3]-29)+15
    y3 = randn(SampleSize[3]-29)
    
    x4 = randn(SampleSize[4]-29)+12.99
    y4 = randn(SampleSize[4]-29)-7.5
    
    x5 = randn(SampleSize[5]-29)+7.5
    y5 = randn(SampleSize[5]-29)-12.99
    
    plt.ion()
    
    if(i%6 == 0):
        drawnow(makeFig)
        plt.pause(.000000000001) 
    """
    ##for i in range(0,6):
     ##   print pv[i]
    ##for i in range(0,6):
      ##  pv[i] = int(dataArray[i])
    
    
    ##for i in range(0,6):
    ##    print dataArray[i]
    ##pv = int(dataArray[0])
    ##print data
    ##print type(data)
   
    ##for i in range(0,6):
      ##  pv[i] = 1
    
    ##for i in range(0,6):
    
    """
    while(arduinoSerialData.readline() != 'TS'):
        pass
    
    for i in range(0,6):
        myData[i] = arduinoSerialData.readline()
        
        
    print '----------------------'
    for i in range(0,6):
        print myData[i] 
    
    print '----------------------'
    """    
        
    """
    myData = arduinoSerialData.readline()
    i = i + 1
    pv = float(myData)
    p= pv*5
    
    if(p<45):
        SampleSize =18*math.exp(0.2*p) 
    else:
        SampleSize =18*math.exp(0.2*45)    
    
    
    x1 = randn(SampleSize-17)
    y1 = randn(SampleSize-17)
    
    
    
         
    print pv
    
    plt.ion()
    if(i%4==0):
        drawnow(makeFig)
        plt.pause(.000000000001) 
    """  
        
        
    