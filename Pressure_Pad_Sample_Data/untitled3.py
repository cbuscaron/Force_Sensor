# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 11:14:23 2014

@author: Camilo
"""

import tables 
from matplotlib import pyplot 
file_name = 'MUN104L.h5' 
file_id = tables.openFile(file_name, mode='r') 
I = file_id.getNode('/I').read() 
file_id.close() 
pyplot.imshow(I, origin='lower', interpolation='nearest') 
pyplot.show()
print I.shape

