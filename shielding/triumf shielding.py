# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 10:48:55 2026

@author: stimp
"""

import numpy as np
from scipy import special
from matplotlib import pyplot as plt

def se(mu_r,sigma,a,b,big_delta,f):
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









#function se_cyl for lab
f=np.logspace(0, 4, 500)
omega=2*np.pi*f
cyli_a=0.10157/2
cyli_b=0.11347/2
cyli_big_delta=cyli_b-cyli_a

se_cyl=se_cylinder(1, 3.8e7, cyli_a, cyli_b, f)
se_cyl_db=20*np.log10(se_cyl)  
 
fig=plt.figure()
ax=fig.add_subplot()
ax.plot(f,se_cyl_db,color="#FF073A")
ax.set_xscale('log')
ax.set_xlabel("frequency (Hz)")
ax.set_ylabel("shielding effectiveness (dB)")
ax.set_ylim(0,100)
ax.grid(True, which="both", ls="--", color='0.65')
#ax.set_title("Al cylinder shielding effectiveness as a function of frequency ")
#ax.legend()
plt.show()












# %%



#function se for copper 
r_0=0.3
cu_big_delta=0.002
cu_a=r_0-cu_big_delta/2
cu_b=r_0+cu_big_delta/2.
se_cu=se(1.09,1.18e7,cu_a,cu_b,cu_big_delta,60)
print("SE for Cu=", se_cu)

#function se for aluminum
h=0.4256
phi=1.077
#if 6 mm thick at 29 Hz SE is ~10
al_a=np.cbrt(3/4*(phi/2-0.006)**2*(h-2*0.006))
al_b=np.cbrt(3*phi**2*h/16)
al_big_delta=al_b-al_a
se_al=se(1,3.8e7,al_a,al_b,al_big_delta,29)
print("SE for Al=", se_al, "\n")

#function se_lab for copper
r_0=0.3
big_delta=0.002
se_cop=se_lab(1.09,1.18e7,cu_a,cu_b,cu_big_delta,60)
print("SE for Cu", se_cop)

#function se_lab for aluminum 
se_alu=se_lab(1,3.8e7,al_a,al_b,al_big_delta,29)
big_delta=al_b-al_a
print("SE for Al=", se_alu, "\n")
#print("a=", a, "b=", b, "big delta=", se_alu_big_delta, "\n")



# %%


# graphing copper (se_lab and se) vs f                                                            
#f=np.logspace(0, 5, 500)
#omega=2*np.pi*f
#se_cu=se(1.09,1.18e7,cu_a,cu_b,cu_big_delta,f)
#se_cop=se_lab(1.09,1.18e7,cu_a,cu_b,cu_big_delta,f)
#se_cu_db=20*np.log10(se_cu)  
#se_cop_db= 20*np.log10(se_cop)  

#fig=plt.figure()
#ax=fig.add_subplot()
#ax.plot(f,se_cu_db,label="se function", color="red")
#ax.plot(f,se_cop_db,linestyle="--",label="se lab function", color="green")
#ax.set_xscale('log')
#ax.set_xlabel("frequency in Hz")
#ax.set_ylabel("SE in dB")
#ax.set_ylim(-15, 85)
#ax.grid(True, which="both", ls="--", color='0.65')
#ax.set_title("copper se and se_lab functions")
#ax.legend()
#plt.show()



# %%


#graphing aluminum (se_lab and se) vs f



f=np.logspace(0, 5, 500)
omega=2*np.pi*f
se_al=se(1,3.8e7,al_a,al_b,al_big_delta,f)
se_alu=se_lab(1,3.8e7,al_a,al_b,al_big_delta,f)
se_al_db=20*np.log10(se_al)  
se_alu_db= 20*np.log10(se_alu)

fig=plt.figure()
ax=fig.add_subplot()
ax.plot(f,se_al_db,label="se function", color="blue")
ax.plot(f,se_alu_db, linestyle="--",label="se lab function", color="orange")
ax.set_xscale('log')
ax.set_xlabel("frequency in Hz")
ax.set_ylabel("SE in dB")
ax.set_ylim(-15, 85)
ax.grid(True, which="both", ls="--", color='0.65')
ax.set_title("aluminum SE vs frequency")
ax.legend()
plt.show()



#finding exact value
target_y=20
found_x=np.interp(target_y, se_al_db,f)
print("aluminum SE vs frequency graph")
print(f"when SE reaches {target_y} dB, frequency is {found_x} Hz", "\n")


# %%


#graphing f vs delta


f=np.logspace(0, 5, 500)
omega=2*np.pi*f
mu_0=4*np.pi*1e-7
mu_r=1
sigma=3.8e7
delta=np.sqrt(2/(omega*mu_0*mu_r*sigma))


fig=plt.figure()
ax=fig.add_subplot()
ax.plot(f,delta)
ax.set_xscale('log')
ax.set_xlabel("frequency in Hz")
ax.set_ylabel("skin depth in m")
ax.grid(True, which="both", ls="--", color='0.65')
ax.set_title("aluminum skin depth vs frequency")
plt.show()



#finding exact value
target_x=29 
found_y=np.interp(target_x, f,delta)
print("aluminum skin depth vs frequency graph")
print(f"at {target_x} Hz, skin depth is {found_y} m")

#double check 
#f=60
#omega=2*np.pi*f
#mu_0=4*np.pi*1e-7
#mu_r=1
#sigma=3.8e7
#delta=np.sqrt(2/(omega*mu_0*mu_r*sigma))
#print(f"delta at 60Hz = {delta} m")
