# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 12:10:17 2014

@author: Camilo B.
"""

from matplotlib.colors import LogNorm
from pylab import *
import random
import numpy as np

p = 0 # 0-40
#x = randn(1000000)
#print len(x)

#y = randn(1000000)

SampleSize =22.67*math.exp(0.2855*p)

x = np.random.uniform(-p/15, p/15, size=SampleSize)
y = np.random.uniform(-p/20, p/20, size=SampleSize)


figure()
hist2d(x, y, bins=50,range=np.array([(-4, 4), (-4, 4)]))
xlim([-4, 4])
ylim([-4, 4])
colorbar()
show()