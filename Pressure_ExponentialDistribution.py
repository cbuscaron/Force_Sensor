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

x = randn(SampleSize)
y = randn(SampleSize)

data = np.random.random((SampleSize-10, SampleSize-10))
    
    

##plt.hist2d(x, y, bins=150,range=np.array([(-6, 6), (-6, 6)]))
plt.hist(x,bins=50)
##colorbar()
xlim([-5, 5])
ylim([0, 40])
##colorbar()

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.1, .95, 0.65, 0.03], axisbg=axcolor)
sfreq = Slider(axfreq, 'Force(N)', 0, 40.0, valinit=0.0)

##plt.ion()


def update(val):
    ##amp = samp.val
    p = sfreq.val
    SampleSize =2*math.exp(0.16*p)

    ##x = np.random.uniform(-p/15, p/15, size=SampleSize)
    
    ##y = np.random.uniform(-p/20, p/20, size=SampleSize)
    ##figure(figsize=(10,10))
    
    x = randn(SampleSize-10)
    y = randn(SampleSize-10)
    ##data = np.random.random((SampleSize-10, SampleSize-10))
    ##plt.cla()    
    plt.subplot()
    plt.hist(x, bins = 100)
    ##pyplot.imshow(data, origin='lower', interpolation='nearest') 
    xlim([-5, 5])
    ylim([0, 40])
##colorbar()

    
    
    ##plt.hist2d(x, y, bins=50,range=np.array([(-5, 5), (-5, 5)]))
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