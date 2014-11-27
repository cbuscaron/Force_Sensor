# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 17:23:26 2014

@author: Camilo
"""

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



##figure(figsize=(10,10))
plt.hist2d(x, y, bins=150,range=np.array([(-5, 5), (-5, 5)]))
xlim([-5, 5])
ylim([-5, 5])
colorbar()

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.1, .95, 0.65, 0.03], axisbg=axcolor)
sfreq = Slider(axfreq, 'Force(N)', 0, 40.0, valinit=0.0)

plt.ion()


def update(val):
    ##amp = samp.val
    p = sfreq.val
    SampleSize =15*math.exp(0.3*p)

    ##x = np.random.uniform(-p/15, p/15, size=SampleSize)
    
    ##y = np.random.uniform(-p/20, p/20, size=SampleSize)
    ##figure(figsize=(10,10))
    
    x = randn(SampleSize)
    y = randn(SampleSize)
    
    ##plt.subplot()
    ##plt.hist2d(x, y, bins=50,range=np.array([(-5, 5), (-5, 5)]))
    at_hist, xedges, yedges = np.histogram2d(x, y, bins=350)
    extent = [yedges[0], yedges[-1], xedges[0], xedges[-1]]

    ##plt.figure()
    plt.subplot()    
    plt.imshow(at_hist, extent=extent, origin='lower', aspect='auto')
    
    
    
    ##fig.canvas.draw_idle()
sfreq.on_changed(update)
##samp.on_changed(update)


##show()