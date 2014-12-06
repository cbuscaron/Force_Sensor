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
time.sleep(1.5)


p = 0.0 # 0-40


SampleSize =22.67*math.exp(0.2855*p)

x = randn(SampleSize-21)
y = randn(SampleSize-21)
 

plt.hist2d(x, y, bins=150,range=np.array([(-25, 25), (-25, 25)]))
colorbar()


i = 0
t = 0

myData = range(6)

##print len(myData)

##for i in range(0,6):
##    print myData[i]
    
    
    
    
##arduinoSerialData.close()
"""
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
"""   
    
    

while True:
    while (arduinoSerialData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    
    data = arduinoSerialData.readline() 
    print data
    ts = 'TS'
    if(data == ts):
        print 'If State'
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
        
        
    