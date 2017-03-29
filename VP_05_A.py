# simulates a binary star system

from __future__ import division
from visual import *
from visual.graph import * # import graphing features

scene = display(background=color.white)

t = 0
dt = 10000

G = 6.67e-11
m1 = 2e30  #star mass in kg
m2 = 1e30

# orbit = 15 days
Torbit = 1296000 # seconds
omega = 2*pi/Torbit

r = (G*(m1+m2)/(omega**2))**(1/3)
r1 = r/3 
r2 = 2*r/3 




star1 = sphere(radius=(3/4*m1/pi)/10e20, color=(1,.3,.15),
               make_trail = True)



star2 = sphere(radius= (3/4*m2/pi)/10e20, color=(1,.8,0),
               make_trail = True)

mass_center = sphere(radius= (3/4*(m2+m2)/2/pi)/10e20, color=(0.7,0.7,0.7),
               make_trail = True)
otherr = sphere(radius= (3/4*(m2+m2)/2/pi)/10e20, color=color.blue,
               make_trail = True)

star1.pos = vector(r1,0,0)
star2.pos = vector(-r2,0,0)
otherr.pos = star1.pos-star2.pos



#graphics
graph_mom1 = gdisplay(height=300,x=430,background=color.white, foreground=color.black)
graph_mom2 = gdisplay(height=300,x=430,y=300,background=color.white, foreground=color.black)
graph_momtot = gdisplay(height=300,x=430,y=600,background=color.white, foreground=color.black)
mom1 = gcurve(color=star1.color, gdisplay = graph_mom1)
mom2 = gcurve(color=star2.color, gdisplay = graph_mom2)
momtot = gcurve(color=color.orange, gdisplay = graph_momtot)

arrows = display(y=400, background=color.white)
#momentum arrows
star1_mom_arrow = arrow(axis=vector(0,0,0),color=star1.color)
star2_mom_arrow = arrow(axis=vector(0,0,0),color=star2.color)
stars_mom_arrow = arrow(axis=vector(0,0,0),color=star2.color)

rcheck = star1.pos-star2.pos
print 'check', rcheck

vert = 1e34
err = 0  #[0,1]
star1_mom = vector(0,m1*sqrt(G*m2*r1*(1+err)/r**2),vert)
star2_mom = vector(0,-m2*sqrt(G*m1*r2*(1+err)/r**2),vert)
print star1_mom
#print star2_mom



# 1296000

while (t< 4*1296000):
    rate(50)
    r = star1.pos-star2.pos
   
    
    f_grav = G*(m1*m2)/mag2(r)*norm(r)
   # print t, r, mag(r)
    star1_mom = star1_mom - f_grav*dt
    star2_mom = star2_mom + f_grav*dt
    star1.pos = star1.pos + star1_mom/m1*dt
    star2.pos = star2.pos + star2_mom/m2*dt

    mass_center.pos = (m1*star1.pos+m2*star2.pos)/(m1+m2)
    otherr.pos = star1.pos-star2.pos

    star1.pos = star1.pos - mass_center.pos
    star2.pos = star2.pos - mass_center.pos
    #graphic updates
    mom1.plot(pos=(t,star1_mom.x))
    mom2.plot(pos=(t,star2_mom.x))
    momtot.plot(pos=(t,star1_mom.x+star2_mom.x))
 #0   scene.center = (mass_center.pos - vector(0,0,0))/2
    #arrows
    star1_mom_arrow.axis = star1_mom
    star2_mom_arrow.axis = star2_mom
    star2_mom_arrow.pos = star1_mom
    stars_mom_arrow.axis = star1_mom + star2_mom
    star1_mom_arrow.shaftwidth = 0.05*star1_mom_arrow.length
    star2_mom_arrow.shaftwidth = 0.05*star2_mom_arrow.length
    stars_mom_arrow.shaftwidth = 0.05*stars_mom_arrow.length

    t = t + dt

print mag(star1_mom)
