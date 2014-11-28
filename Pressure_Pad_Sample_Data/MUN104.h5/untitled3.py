# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 11:14:23 2014

@author: Camilo
"""
"""
import tables 
from matplotlib import pyplot 
import numpy as np
"""

"""
file_name = 'MUN104L.h5' 
file_id = tables.openFile(file_name, mode='r') 
I = file_id.getNode('/I').read() 
file_id.close() 
print len(I)
pyplot.imshow(I, origin='lower', interpolation='nearest') 
pyplot.colorbar()
pyplot.show()
"""
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
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def main():
    # Generate some random data
    nx, ny = 100, 100
    data = np.ones((ny,nx))

    # Define a circle in the center of the data with a radius of 20 pixels
    radius = 20
    center_x = nx // 2
    center_y = ny // 2

    plot_masked(data, center_x, center_y, radius)
    ##plot_clipped(data, center_x, center_y, radius)
    nx, ny = 100, 100
    data = np.zeros((ny,nx))

    # Define a circle in the center of the data with a radius of 20 pixels
    radius = 40
    center_x = nx // 2
    center_y = ny // 2
    
    plt.subplot()
    plot_masked(data, center_x, center_y, radius)
    
    plt.show()

def plot_masked(data, center_x, center_y, radius):
    """Plots the image masked outside of a circle using masked arrays"""
    # Calculate the distance from the center of the circle
    ny, nx = data.shape
    print ny
    print nx
    ix, iy = np.meshgrid(np.arange(nx), np.arange(ny))
    print ix
    print iy
    
    distance = np.sqrt((ix - center_x)**2 + (iy - center_y)**2)

    # Mask portions of the data array outside of the circle
    data = np.ma.masked_where(distance > radius, data)
    print data
    # Plot
    ##plt.figure()
    plt.imshow(data)
    plt.colorbar()
    plt.title('Masked Array')

def plot_clipped(data, center_x, center_y, radius):
    """Plots the image clipped outside of a circle by using a clip path"""
    fig = plt.figure()
    ax = fig.add_subplot(111)

    # Make a circle
    circ = patches.Circle((center_x, center_y), radius, facecolor='none')
    ax.add_patch(circ) # Plot the outline

    # Plot the clipped image
    im = ax.imshow(data, clip_path=circ, clip_on=True)

    plt.title('Clipped Array')

main()
