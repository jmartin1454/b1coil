
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 09:12:23 2026

@author: stimp
"""
import math
import numpy as np

x= 1
y= math.sqrt(3)
z=(x + y*1j)/2

z2= complex(x,y)/2

print(z2)
print(np.real(z))
print(np.imag(z))


from matplotlib import pyplot as plt


def gen_fig(figsize=(2,2), xlim=[0,1], ylim=[0,1]):
    #generating figure to plot complex numbers
    plt.figure(figsize=figsize)
    plt.grid()
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel('Re')
    plt.ylabel('Im')
    
def plot_vector(z, color='k', start=0, linestyle='-'):
    return plt.arrow(np.real(start), np.imag(start), np.real(z), np.imag(z), 
                     linestyle=linestyle, head_width=0.05, fc=color, ec=color,
                      overhang=0.3, 
                      
                      length_includes_head=True)


z=(x + y*1j)/2


gen_fig(figsize=(7.5, 3), xlim=[0, 1], ylim=[0, 1])
v = plot_vector(z, color='k')

plt.text(x/2, y/2,'$z$', size='16')


#for modulus of complex number
print("modulus:", np.abs(z))
print("angle (in radians):", np.angle(z))
print("angle (in degrees):", 180*np.angle(z)/np.pi)
# another way to get angle in degrees
# print("angle (in degrees):", np.rad2deg(np.angle(z)))


theta=np.angle(z)
mod=np.abs(z)
print("x=", (mod*math.cos(theta)))
print("y=", (mod*math.sin(theta)))
print("r=", (math.sqrt((np.real(z)**2)+(np.imag(z)**2))))
#another way to get x, y, and r lengths 

#for conjugate of z
print(np.conj(z))

print(z*np.conj(z))
print(np.conj(z)*z)

