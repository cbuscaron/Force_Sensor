# -*- coding: utf-8 -*-
"""
Created on Wed Nov 26 12:10:17 2014

@author: Camilo B.
"""

from matplotlib.colors import LogNorm
from pylab import *

#normal distribution center at x=0 and y=5
x = randn(50000)
print len(x)

y = randn(50000)
figure()
hist2d(x, y, bins=50,range=np.array([(-4, 4), (-4, 4)]))
xlim([-4, 5])
ylim([-4, 4])
colorbar()
show()