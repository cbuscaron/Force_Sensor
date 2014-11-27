# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 09:41:17 2014

@author: Camilo
"""

from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
from numpy.random import randn

#normal distribution center at x=0 and y=5
x = randn(100000)
y = randn(100000)+5

H, xedges, yedges, img = plt.hist2d(x, y, norm=LogNorm())
extent = [yedges[0], yedges[-1], xedges[0], xedges[-1]]
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
im = ax.imshow(H, cmap=plt.cm.jet, extent=extent, norm=LogNorm())
fig.colorbar(im, ax=ax)
plt.show()