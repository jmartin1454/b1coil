#!/usr/bin/python3

# Fri May 24 10:11:45 CDT 2019 Jeff added this line.
# June 16, 2019 Jeff modified to limit to class definitions.

from scipy.constants import mu_0, pi
import numpy as np
from patch import *
import matplotlib.pyplot as plt




def brectangle(z,a,b,i):
    return mu_0*i/(4*pi)*a*b/sqrt((a/2)**2+(b/2)**2+z**2)*(
        1/((b/2)**2+z**2)+1/((a/2)**2+z**2)
        )


# # Halliday & Resnick, 10th ed., question 29.83
# print("This next one is question 29.83")

# a = 0.08
# i = 10.0
# p0 = np.array([0,0,0])
# p1 = np.array([a,0,0])
# p2 = np.array([a,-a,0])
# p3 = np.array([0,-a,0])
# points = (p0,p1,p2,p3)
# r = np.array([a/4,-a/4,0])
# print(b_loop(i,points,r))



# btot = 2*mu_0 *i*sqrt(a**2 + b**2)/(pi*a*b)


## repeat of 29.83:
#thiscoil = coil(points,i)
#print(thiscoil.b(r))
#thiscoil.set_current(i/2.0)
#print(thiscoil.b(r))
#print(thiscoil.b_prime(0,0,0))

# cs = coilset()
# cs.add_coil(points)
# import matplotlib.pyplot as plt



a = 0.08 # m
b = 0.1 # m
s = 0.09 # m -- separation of the two coils
i = 1.0 # A
p0 = np.array([a/2,b/2,0])
p1 = np.array([-a/2,b/2,0])
p2 = np.array([-a/2,-b/2,0])
p3 = np.array([a/2,-b/2,0])
points = (p0,p1,p2,p3)
r = np.array([0,0,0])
print(b_loop(i,points,r))
print(brectangle(0,a,b,i))

print("Test of b_segment")
print(b_segment(i,p0,p1,r))
print(mu_0*i*a/(4*pi*b/2)/sqrt((a/2)**2+(b/2)**2))
print(2*mu_0*i*a/(4*pi*b/2)/sqrt((a/2)**2+(b/2)**2)+2*mu_0*i*b/(4*pi*a/2)/sqrt((a/2)**2+(b/2)**2))
print("End test of b_segment")


fig2 = plt.figure()
ax2=fig2.add_subplot()
z=np.linspace(-1,1,201)
print(z)
bs=brectangle(z,a,b,i)
print(bs)
print(len(bs))
ax2.plot(z,bs)

cs = coilset()
p0 = np.array([a/2,b/2,-s/2])
p1 = np.array([-a/2,b/2,-s/2])
p2 = np.array([-a/2,-b/2,-s/2])
p3 = np.array([a/2,-b/2,-s/2])
points = (p0,p1,p2,p3)
cs.add_coil(points)
p0 = np.array([a/2,b/2,s/2])
p1 = np.array([-a/2,b/2,s/2])
p2 = np.array([-a/2,-b/2,s/2])
p3 = np.array([a/2,-b/2,s/2])
points = (p0,p1,p2,p3)
cs.add_coil(points)
fig = plt.figure()
ax=fig.add_subplot(111,projection='3d')
cs.draw_coils(ax)
cs.set_common_current(i)
x=z
print(x)
bps=cs.b_prime(0,0,z)
print(bps[0])
print(bps[1])
print(bps[2])
bp_z=bps[2]
ax2.plot(z,bp_z,'--')

fig3 = plt.figure()
ax3=fig3.add_subplot()
gridpoints=np.linspace(-.1,.1,201)
y,z=np.meshgrid(gridpoints,gridpoints)
bps_mesh=cs.b_prime(0,y,z)
bmod_mesh=sqrt(bps_mesh[0]**2+bps_mesh[1]**2+bps_mesh[2]**2)
im3=ax3.pcolormesh(y,z,bmod_mesh,vmax=1e-4)
fig3.colorbar(im3,ax=ax3)

plt.show()
