# -*- coding: utf-8 -*-
"""
Created on Thu Nov 27 13:41:48 2014

@author: Camilo
"""

from drawnow import drawnow

x = zeros((N,N))

def function_to_draw_figure():
    #figure() # don't call, otherwise new window opened
    imshow(x) # python's global scope
    #show()   # don't call show()!

ion() # enable interactivity, can be default
figure()
for i in arange(x):
    x.flat[i] = 1
    drawnow(function_to_draw_figure)