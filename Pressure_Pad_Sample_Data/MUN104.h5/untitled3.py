# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 11:14:23 2014

@author: Camilo
"""

import tables 
from matplotlib import pyplot 
import numpy as np



file_name = 'MUN104L.h5' 
file_id = tables.openFile(file_name, mode='r') 
I = file_id.getNode('/I').read() 
file_id.close() 
print len(I)
pyplot.imshow(I, origin='lower', interpolation='nearest') 
pyplot.colorbar()
pyplot.show()
print I.shape

"""
N = 50

grid = np.zeros((N,N))
R = 10
Y = 5

for x in range(5):
    grid[((N-1)/2)+x][((N-1)/2)+x] = R
    grid[((N-1)/2)-x][((N-1)/2)-x] = R
    grid[((N-1)/2)+x][((N-1)/2)-x] = R
    grid[((N-1)/2)-x][((N-1)/2)+x] = R
    
    grid[((N-1)/2)][((N-1)/2)+x] = R
    grid[((N-1)/2)][((N-1)/2)-x] = R
    grid[((N-1)/2)+x][((N-1)/2)] = R
    grid[((N-1)/2)-x][((N-1)/2)] = R


for x in range(5,10):
    grid[((N-1)/2)+x][((N-1)/2)+x] = Y
    grid[((N-1)/2)-x][((N-1)/2)-x] = Y
    grid[((N-1)/2)+x][((N-1)/2)-x] = Y
    grid[((N-1)/2)-x][((N-1)/2)+x] = Y
    
    grid[((N-1)/2)][((N-1)/2)+x] = Y
    grid[((N-1)/2)][((N-1)/2)-x] = Y
    grid[((N-1)/2)+x][((N-1)/2)] = Y
    grid[((N-1)/2)-x][((N-1)/2)] = Y


##print grid    
pyplot.imshow(grid, origin='lower', interpolation='nearest') 
pyplot.colorbar()
pyplot.show()    

"""