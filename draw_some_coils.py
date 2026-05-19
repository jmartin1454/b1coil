#!/usr/bin/python3

# Fri May 24 10:11:45 CDT 2019 Jeff added this line.
# June 16, 2019 Jeff modified to limit to class definitions.

from scipy.constants import mu_0, pi
import numpy as np
from patch import *


# Halliday & Resnick, 10th ed., question 29.83
print("This next one is question 29.83")

a = 20.0
b = 10.0
i = 10.0
p0 = np.array([-a/2,b/2,0])
p1 = np.array([a/2,b/2,0])
p2 = np.array([a/2,-b/2,0])
p3 = np.array([-a/2,-b/2,0])
points = (p0,p1,p2,p3)
r = np.array([0,0,0])
print(b_loop(i,points,r))


btot = 2*mu_0 *i*sqrt(a**2 + b**2)/(pi*a*b)
print(btot)

## repeat of 29.83:
#thiscoil = coil(points,i)
#print(thiscoil.b(r))
#thiscoil.set_current(i/2.0)
#print(thiscoil.b(r))
#print(thiscoil.b_prime(0,0,0))

cs = coilset()
cs.add_coil(points)
import matplotlib.pyplot as plt
fig = plt.figure()
ax=fig.add_subplot(111,projection='3d')
cs.draw_coils(ax)
plt.show()



