## -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 13:19:31 2014

@author: Camilo
"""

from matplotlib import pyplot as PLT
from matplotlib import cm as CM
from matplotlib import mlab as ML
import numpy as NP

##n = 1e5

SampleSize =22.67*math.exp(0.21*40)

    ##x = np.random.uniform(-p/15, p/15, size=SampleSize)
    
    ##y = np.random.uniform(-p/20, p/20, size=SampleSize)
    ##figure(figsize=(10,10))
    
x = randn(SampleSize-21)
y = randn(SampleSize-21)

##x = y = NP.linspace(-5, 5, 100)


# if 'bins=None', then color of each hexagon corresponds directly to its count
# 'C' is optional--it maps values to x-y coordinates; if 'C' is None (default) then 
# the result is a pure 2D histogram 

PLT.hexbin(x, y,gridsize=30, cmap=CM.jet, bins=None)
PLT.axis([x.min(), x.max(), y.min(), y.max()])

#cb = PLT.colorbar()
#cb.set_label('mean value')

#PLT.show() 