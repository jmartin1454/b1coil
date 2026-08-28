# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 13:50:24 2026

@author: stimp
"""

import pandas as pd
import numpy as np
from scipy import special
from matplotlib import pyplot as plt




def se_cylinder(mu_r,sigma,a,b,f):
    mu_0=4*np.pi*1e-7
    omega=2*np.pi*f
    delta=np.sqrt(2/(omega*mu_0*mu_r*sigma))
    gamma=(1+1j)/delta
    u=gamma*a
    v=gamma*b
    k1deru=-(special.kve(0,u)+special.kve(2,u))/2
    i1deru=(special.ive(0,u)+special.ive(2,u))/2
    k1derv=-(special.kve(0,v)+special.kve(2,v))/2
    i1derv=(special.ive(0,v)+special.ive(2,v))/2
    pt1 = mu_r*special.kve(1,u) - u*k1deru
    pt2 = mu_r*special.ive(1,v) + v*i1derv
    pt3 = mu_r*special.ive(1,u) - u*i1deru
    pt4 = mu_r*special.kve(1,v) + v*k1derv
    se=np.abs(a/(2*b*mu_r)*(np.exp(-u+np.real(v))*pt1*pt2-np.exp(np.real(u)-v)*pt3*pt4))
    return se

def se_lab(mu_r,sigma,a,b,big_delta,f):
    mu_0=4*np.pi*1e-7
    big_delta=b-a
    omega=2*np.pi*f
    delta=np.sqrt(2/(omega*mu_0*mu_r*sigma))
    gamma=(1+1j)/delta
    q=1/(3*b**3*gamma**2*mu_r)
    p=3*b-big_delta
    k=a*b*gamma**2-1
    l=a**2*b**2*gamma**2+b**2-a*big_delta
    o=gamma*big_delta
    se=np.abs(q*(2*big_delta*mu_r**2+mu_r*(a*b*p*gamma**2-big_delta)+big_delta*k)*np.cosh(o)
                 +q/gamma*(gamma**2*l+p*big_delta*mu_r*gamma**2+2*k*mu_r**2+mu_r+1)*np.sinh(o))
    return se








#function se_cyl from paper + graph
f=np.logspace(0, 5, 500)
omega=2*np.pi*f
r_0=0.3
cyl_big_delta=0.00015
cyl_a=r_0-cyl_big_delta/2
cyl_b=r_0+cyl_big_delta/2

se_cyl=se_cylinder(75e3, 2e6, cyl_a, cyl_b, f)
se_cyl_db=20*np.log10(se_cyl)  
 
fig=plt.figure()
ax=fig.add_subplot()
ax.plot(f,se_cyl_db,label="se_cyl function", color="red")
ax.set_xscale('log')
ax.set_xlabel("frequency in Hz")
ax.set_ylabel("SE in dB")
ax.set_ylim(0,350)
ax.grid(True, which="both", ls="--", color='0.65')
ax.set_title("cylinder se functions")
ax.legend()
plt.show()






#SE for Al cylinder model
f=np.logspace(0, 4, 500)
omega=2*np.pi*f
cyli_a=0.10157/2
cyli_b=0.11347/2
cyli_big_delta=cyli_b-cyli_a

se_cylinder=se_cylinder(1, 3.8e7, cyli_a, cyli_b, f)
se_cylinder_db=20*np.log10(se_cylinder)  
 
fig=plt.figure()
ax=fig.add_subplot()
ax.plot(f,se_cylinder_db,color='#FF073A')
ax.set_xscale('log')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Shielding effectiveness (dB)')
ax.set_ylim(0,100)
ax.grid(True, which='both', ls='--', color='0.65')
#ax.set_title("Al cylinder shielding effectiveness as a function of frequency ")
#ax.legend()
#plt.show()





#SE for Al sphere model
sph_a=0.10157/2
sph_b=0.11347/2
sph_big_delta=sph_b-sph_a

se_sphere=se_lab(1,3.8e7,sph_a,sph_b,sph_big_delta,f)
se_sphere_db=20*np.log10(se_sphere)  




#graph of lab data By and Bx vs Al model cylinder
df=pd.read_excel(r'C:\Users\stimp\onedrive\desktop\university\research\B1 data.xlsx', header=83, usecols='D:H')

fig2=plt.figure()
ax2=fig2.add_subplot()
se_bx=20*np.log10(df['SE of Bx'])
se_by=20*np.log10(df['SE of By'])

ax2.plot(df['frequency (Hz)'],se_bx, label='Bx',color='blue')
ax2.plot(df['frequency (Hz)'],se_by, label='By',color='orange')
ax2.plot(f,se_cylinder_db,label='Cylinder Model',color='#FF073A')
ax2.plot(f,se_sphere_db,label='Sphere Model',color='#4CBB17')

ax2.set_xscale('log')
ax2.set_xlabel('Frequency (Hz)')
ax2.set_ylabel('Shielding effectiveness (dB)')
ax2.set_ylim(0,100)
ax2.grid(True, which='both', ls='--', color='0.65')
ax2.legend()
plt.show()







