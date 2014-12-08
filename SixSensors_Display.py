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
import ast



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

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def makeFig():
    plt.subplot()
    plt.hist2d(x, y, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())  
    
    plt.hist2d(x1, y1, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
    plt.hist2d(x2, y2, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
    plt.hist2d(x3, y3, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
    plt.hist2d(x4, y4, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
    plt.hist2d(x5, y5, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())




while True:
    while (arduinoSerialData.inWaiting()==0): #Wait here until there is data
        pass #do nothing
    
    arduinoString = arduinoSerialData.readline()
    dataArray = arduinoString.split(',')
    t = t + 1
    
    ##print len(dataArray)
    ##for i in range(0,6):
    ##    pv[i] = ast.literal_eval(dataArray[i])\
    print len(dataArray)
    if(len(dataArray) == 7):
        for i in range(0,6):
            pv[i] = int(dataArray[i])
        
        for i in range(0,6):
            if(pv[i]<40):
                SampleSize[i] =int(20*math.exp(0.2*pv[i]))
            else:
                SampleSize[i] =int(20*math.exp(0.2*40))
    
    
        x = randn(SampleSize[0]-19)
        y = randn(SampleSize[0]-19)+15
        
        x1 = randn(SampleSize[1]-19)+7.5
        y1 = randn(SampleSize[1]-19)+12.99
        
        x2 = randn(SampleSize[2]-19)+12.99
        y2 = randn(SampleSize[2]-19)+7.5
        
        x3 = randn(SampleSize[3]-19)+15
        y3 = randn(SampleSize[3]-19)
        
        x4 = randn(SampleSize[4]-19)+12.99
        y4 = randn(SampleSize[4]-19)-7.5
        
        x5 = randn(SampleSize[5]-19)+7.5
        y5 = randn(SampleSize[5]-19)-12.99
        
        plt.ion()
        
        for i in range(0,6):
            print SampleSize[i]
        
        """
        if(t%4 == 0):
            print t
         ##   drawnow(makeFig)
            
            ##plt.hist2d(x, y, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())  
    
            ##plt.hist2d(x1, y1, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
            ##plt.hist2d(x2, y2, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
            ###plt.hist2d(x3, y3, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
            ##plt.hist2d(x4, y4, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
            ##plt.hist2d(x5, y5, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())   
         
            plt.pause(.000000000001) 
            ##for i in range(0,6):
            ##    print pv[i]
        """
    else:   
         print 'skip'
    """        
    if(isfloat(dataArray[0])):
        pv[0]= int(dataArray[0])
        print pv[0]
    else:
        print 'XXX'
    
    if(isfloat(dataArray[1])):
        pv[1]= int(dataArray[1])
        print pv[1]
    else:
        print 'XXX'
    
    if(isfloat(dataArray[2])):
        pv[2]= int(dataArray[2])
        print pv[2]
    else:
        print 'XXX'
    
    if(isfloat(dataArray[3])):
        pv[3]= int(dataArray[3])
        print pv[3]
    else:
        print 'XXX'
    
    if(isfloat(dataArray[4])):
        pv[4]= int(dataArray[4])
        print pv[4]
    else:
        print 'XXX'
    
    if(isfloat(dataArray[5])):
        pv[5]= int(dataArray[5])
        print pv[5]
    else:
        print 'XXX'
    """
    """
    for i in range(0,6):
        if(pv[i]<45):
            SampleSize[i] =30*math.exp(0.2*pv[i])
        else:
            SampleSize[i] =30*math.exp(0.2*pv[i])
    
    for i in range(0,6):
        print SampleSize[i]
    """
    """
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
    
    if(i%10 == 0):
        drawnow(makeFig)
        plt.pause(.01) 
    """
    """
    pv[0] = ast.literal_eval(dataArray[0])
    pv[1] = ast.literal_eval(dataArray[1])
    pv[2] = ast.literal_eval(dataArray[2])
    pv[3] = ast.literal_eval(dataArray[3])
    pv[4] = ast.literal_eval(dataArray[4])
    pv[5] = ast.literal_eval(dataArray[5])
    
    
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

        
    