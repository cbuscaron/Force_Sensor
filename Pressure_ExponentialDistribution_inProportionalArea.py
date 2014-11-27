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

p = 0.0 # 0-40
#x = randn(1000000)
#print len(x)t

#y = randn(1000000)

SampleSize =22.67*math.exp(0.2855*p)

x = np.random.uniform(-p/15, p/15, size=SampleSize)
y = np.random.uniform(-p/20, p/20, size=SampleSize)


##figure(figsize=(10,10))
hist2d(x, y, bins=50,range=np.array([(-4, 4), (-4, 4)]))
xlim([-4, 4])
ylim([-4, 4])
colorbar()

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.1, .95, 0.65, 0.03], axisbg=axcolor)
sfreq = Slider(axfreq, 'Freq', 0, 40.0, valinit=0.0)

def update(val):
    ##amp = samp.val
    p = sfreq.val
    SampleSize =22.67*math.exp(0.2855*p)

    x = np.random.uniform(-p/15, p/15, size=SampleSize)
    y = np.random.uniform(-p/20, p/20, size=SampleSize)
    ##figure(figsize=(10,10))
    plt.subplot()
    hist2d(x, y, bins=50,range=np.array([(-4, 4), (-4, 4)]))
    
    
    fig.canvas.draw_idle()
sfreq.on_changed(update)
##samp.on_changed(update)


##show()