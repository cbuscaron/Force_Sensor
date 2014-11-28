# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 13:13:57 2014

@author: Camilo
"""

from pylab import *
import numpy as np
from scipy.interpolate import griddata

#create 5000 Random points distributed within the circle radius 100
max_r = 100
max_theta = 2.0 * np.pi
number_points = 5000
points = np.random.rand(number_points,2)*[max_r,max_theta]

#Some function to generate values for these points, 
#this could be values = np.random.rand(number_points)
values = points[:,0] * np.sin(points[:,1])* np.cos(points[:,1])

#now we create a grid of values, interpolated from our random sample above
theta = np.linspace(0.0, max_theta, 100)
r = np.linspace(0, max_r, 200)
grid_r, grid_theta = np.meshgrid(r, theta)
data = griddata(points, values, (grid_r, grid_theta), method='cubic',fill_value=0)

#Create a polar projection
ax1 = plt.subplot(projection="polar")
ax1.pcolormesh(theta,r,data.T)
ax1.colorbar()
plt.show()