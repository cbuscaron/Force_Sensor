# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 18:53:56 2014

@author: Camilo
"""

from pylab import *
from matplotlib import pyplot as plt
import matplotlib.animation as animation
 
import serial
import time
 
arduino = serial.Serial('com3',115200)
time.sleep(1)
 
fig, axs = plt.subplots(3, 1)
 
t = 0
ys = []
signal = []
threshold = 0.03
dead_time = 10
dead = -dead_time - 1
 
signal_ts = [[],[],[]]
 
for i in range(3):
    ys.append([])
    signal.append([])
 
def do_step():
    global signal, t, dead
    t += 1
    val = arduino.readline()
    vs = val[:-2].split()
    if len(vs) == 6:
        for v, y, sig, sigt in zip([vs[0:2], vs[2:4], vs[4:6]], ys, signal, signal_ts):
            try:
                y.append(max(float(v[0]), float(v[1])))
                if y[-1] > threshold and t - dead > dead_time:
                    sig.append(t)
                    
            except:
                y.append(0)
 
    for i in range(len(ys)):
        ys[i] = ys[i][-100:]
 
    for s in signal:
        if not s:
            break
    else:
        diff1 = signal[0][0] - signal[1][0]
        diff2 = signal[0][0] - signal[2][0]
        if abs(diff1) > 10 or abs(diff2) > 10:
            pass
        else:
            for sig, ts in zip(signal, signal_ts):
                ts.append(sig[0])
 
        signal = [[], [], []]
        dead = t
 
def updatefig(*args):
    for i in range(10):
        do_step()
 
    for ax, y, sigs in zip(axs, ys, signal_ts):
        ax.clear()
 
        ax.axhline(threshold, c='g', ls='--')
        ax.plot(linspace(max(0, t-99), t, len(y)), y, 'b-')
        for s in sigs:
            ax.axvline(s, c='r', ls='-')
 
        for s in sigs:
            if t - s > 100:
                sigs.remove(s)
 
        ax.set_ylim(-0.01, 0.1)
        ax.set_xlim(max(0, t-100), t)
 
    return list(axs)
 
ani = animation.FuncAnimation(fig, updatefig, interval=80, blit=True)
plt.show()