# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:48:55 2026

@author: stimp
"""

import numpy as np
from matplotlib import pyplot as plt



#constants and calculations
mu_0=4*np.pi*(10**-7) #H/m
mu_r=1.00 #relative permeablility of material
sigma=3.5*(10**7) #electrical conductivity of material in S/m
# have to change this still r_0=0.3 #in m'
h=0.4256 #in m
phi=1.2043 #in m
b=np.cbrt(3*phi**2*h/16) #outer radius in m
a=np.cbrt(3/4*(phi/2-0.0254)**2*(h-2*0.0254)) #inner radius in m
big_delta=b-a #wall thickness 
print("big delta=", big_delta)
#f=1
f=np.logspace(0, 5, 500) 
omega=2*np.pi*f
delta=np.sqrt(2/omega*mu_0*mu_r*sigma)
gamma=(1+1j)/delta

e=1/(3*b**3*gamma**2*mu_r)
p=3*b-big_delta
k=a*b*gamma**2-1
l=a**2*b**2*gamma**2+b**2-a*big_delta
o=gamma*big_delta
SE_ee=np.abs(e*(2*big_delta*mu_r**2+mu_r*(a*b*p*gamma**2-big_delta)+big_delta*k)*np.cosh(o)
             +e/gamma*(gamma**2*l+p*big_delta*mu_r*gamma**2+2*k*mu_r**2+mu_r+1)*np.sinh(o))



# graphing SE_ee vs f                                                            
SE_ee_db= 20*np.log10(SE_ee)  
print()

fig=plt.figure()
ax=fig.add_subplot()
ax.plot(f, SE_ee_db, color='red')
ax.set_xscale('log')

ax.set_xlabel("frequency in Hz")
ax.set_ylabel("SE in dB")
ax.set_ylim(-15,85)
ax.set_title("SE exact expression")

ax.grid(True, which="both", ls="--", color='0.65')

plt.show()
