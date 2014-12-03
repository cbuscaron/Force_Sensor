# -*- coding: utf-8 -*-
"""
Created on Wed Dec 03 10:19:22 2014

@author: user
"""
"""
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x, y = np.random.rand(2, 100) * 4
hist, xedges, yedges = np.histogram2d(x, y, bins=4)

elements = (len(xedges) - 1) * (len(yedges) - 1)
xpos, ypos = np.meshgrid(xedges[:-1]+0.25, yedges[:-1]+0.25)

xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros(elements)
dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
plt.colorbar()
plt.show()
"""
from rootpy.interactive import wait
from rootpy.plotting import Canvas, Hist, Hist2D, Hist3D
from rootpy.plotting.style import set_style
import numpy as np
import rootpy

set_style('ATLAS')

c1 = Canvas()
a = Hist(1000, -5, 5)
a.fill_array(np.random.randn(1000000))
a.Draw('hist')

c2 = Canvas()
c2.SetRightMargin(0.1)
b = Hist2D(100, -5, 5, 100, -5, 5)
b.fill_array(np.random.randn(1000000, 2))
b.Draw('LEGO20')

c3 = Canvas()
c3.SetRightMargin(0.1)
c = Hist3D(10, -5, 5, 10, -5, 5, 10, -5, 5)
c.markersize = .3
c.fill_array(np.random.randn(10000, 3))
c.Draw('SCAT')
wait(True)
