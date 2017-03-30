import numpy as np                         ## numpy is a library that inclues most of the numerical funciton you will need
import matplotlib.pyplot as plt            ## this is the library we use to plot
## The next line causes matplot lib it plot in the notebook, rather than poping up a window, for animations turn this off 
%matplotlib inline    
from mpl_toolkits.mplot3d import Axes3D   ## this is a special library to plot in 3d we are using today

import matplotlib.cm as cm

from __future__ import division

from visual import *
from visual.graph import * # import graphing features

N = 15
mol=[]
time=0
w=0
mass = 1.0552061e-25
bond = 255.6e-12  # meters
radius = 135e-12

mom_0 = vector(-1e-22,0,0)

k = 6

scene = display()

for i in range(N):
    mol.append(sphere(pos = vector(2*i*bond,0,0),radius = radius, exist = 1,
            mom = vector(0,0,0),color=color.cyan,
            force = vector(0,0,0),fM = vector(0,0,0),fP = vector(0,0,0)))
print mol

mol[0].mom = mol[1].mom + mom_0

l_0 = 2*bond #mol[6].pos - mol[5].pos

t = 0
dt = 1e-14
while t<1:
    rate(100)
    for M in arange(0,N-1,1):
        mol[M].fM = k*abs(mag(mol[M+1].pos-mol[M].pos)-l_0)*norm(mol[M+1].pos-mol[M].pos)
    for P in arange(1,N,1):
        mol[P].fP = k*abs(mag(mol[P-1].pos-mol[P].pos)+l_0)*norm(mol[P-1].pos-mol[P].pos)
    for k in arange(0,N,1):
            mol[k].force = mol[k].fP + mol[k].fM
            mol[k].mom = mol[k].mom+ mol[k].force *dt
            mol[k].pos = mol[k].pos + mol[k].mom/mass * dt
    #scene.center = mol[0].pos
    #print mol[3].mom
    t = t + dt

    
