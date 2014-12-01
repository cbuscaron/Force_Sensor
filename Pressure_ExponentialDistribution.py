# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 11:19:39 2014

@author: Camilo
"""

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
from matplotlib import pyplot as PLT
from matplotlib import cm as CM

p = 0.0 # 0-40
#x = randn(1000000)
#print len(x)t

#y = randn(1000000)

SampleSize =22.67*math.exp(0.2855*p)
SampleSize2= SampleSize/2

x = np.random.uniform(-p/15, p/15, size=SampleSize)
y = np.random.uniform(-p/20, p/20, size=SampleSize)

x = randn(SampleSize-21)
y = randn(SampleSize-21)

data = np.random.random((SampleSize-10, SampleSize-10))
    
    

plt.hist2d(x, y, bins=150,range=np.array([(-25, 25), (-25, 25)]))
##plt.hist(x,bins=50)
colorbar()
##xlim([-5, 5])
##ylim([0, 40])
##colorbar()

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.1, .95, 0.65, 0.03], axisbg=axcolor)
sfreq = Slider(axfreq, 'Force(N)', 0, 40.0, valinit=0.0)
##plt.clf()
##plt.ion()


def update(val):
    ##amp = samp.val
    p = sfreq.val
    SampleSize =30*math.exp(0.2*p)

    ##x = np.random.uniform(-p/15, p/15, size=SampleSize)
    
    ##y = np.random.uniform(-p/20, p/20, size=SampleSize)
    ##figure(figsize=(10,10))
    
    x1 = randn(SampleSize-10)
    y1 = randn(SampleSize-10)+15
    
    x2 = randn(SampleSize-10)
    y2 = randn(SampleSize-10)-15
    
    x3 = randn(SampleSize-10)-7.5
    y3 = randn(SampleSize-10)+12.99
    
    x4 = randn(SampleSize-10)-12.99
    y4 = randn(SampleSize-10)+7.5
    
    x5 = randn(SampleSize-10)-15
    y5 = randn(SampleSize-10)
    
    print len(x1)
    print len(x2)
    print "X"
    print len(x)
    
    ##data = np.random.random((SampleSize-10, SampleSize-10))
    ##plt.cla()    
    ##plt.subplot()
    ##plt.hist(x, bins = 100)
    ##pyplot.imshow(data, origin='lower', interpolation='nearest') 
    ##xlim([-5, 5])
    ##ylim([0, 40])
##colorbar()

    hold(True)
    plt.subplot()
    plt.hist2d(x1, y1, bins=200,range=np.array([(-25, 25), (-25, 25)]), norm=LogNorm())
    
    hold(True)
    ##plt.subplot()
    plt.hist2d(x2, y2, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
    hold(True)
    plt.hist2d(x3, y3, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
    hold(True)
    plt.hist2d(x4, y4, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    
    hold(True)
    plt.hist2d(x5, y5, bins=200,range=np.array([(-25, 25), (-25, 25)]),norm=LogNorm())
    ##histogram2d
    ##H, xedges, yedges = np.histogram2d(x, y, bins=100,range=np.array([(-10, 10), (-10, 10)]))
    
    ##X, Y = np.meshgrid(xedges, yedges)
    ##plt.pcolormesh(X, Y, H)
    ##plt.set_aspect('equal')
    
    
    
    ##plt.colorbar()
    ##PLT.hexbin(x, y,gridsize=30, cmap=CM.jet, bins=None)
    ##PLT.axis([x.min(), x.max(), y.min(), y.max()])
    ##PLT.axis([-6,6,-6,6])

    ##cb = PLT.colorbar()
    ##cb.set_label('mean value')
    ##PLT.show() 
    
    ##fig.canvas.draw_idle()
sfreq.on_changed(update)
##samp.on_changed(update)


##show()