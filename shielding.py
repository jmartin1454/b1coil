# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:28:48 2026

@author: stimp
"""

import math
import numpy as np 
from matplotlib import pyplot as plt
print()



# reproducing figure B4(copper)

# constants 
mu_0=4*np.pi*(10**-7) #H/m
mu_r=1.09  #relative permeablility of material
sigma=1.18*(10**7) #electrical conductivity of material in S/m
r_0=0.3 #in m
big_delta=0.002 #in m
b=0.020 #outer radius in m
a=0.018 #inner radius in m
#big_delta=b-a   #wall thickness 



#calculating SE (thick shield) with B15-only real numbers
omega=2*np.pi*1
delta= np.sqrt(2/(omega*mu_0*mu_r*sigma)) 
gamma=((1+1j)/delta)
SE_ts=(r_0/(3*math.sqrt(2)*mu_r*delta))*((np.exp(big_delta/delta)))
SE_test=(np.abs(((r_0*gamma*(np.exp(gamma*big_delta)))/(6*mu_r))))
print(SE_test, "should equal", SE_ts)
print("SE thick shield=", SE_ts)
print("omega=", omega)
print("delta=", delta)
print("gamma=", gamma, "\n")




#calculating SE (thick shield) with B15-imaginary numbers
z=(((r_0*gamma/(6*mu_r))*(np.exp(gamma*big_delta))))
z_star=(np.conj(z))
z_mag=(np.sqrt(z*z_star))
real_z_mag=(np.real(z_mag))
print("z=", z)
print("z star=", z_star)
#another way to get z magnitude: print("z mag./mod=", np.abs(z))
print("z mag=", z_mag)
print("real z mag=", real_z_mag, "\n")



#calculating SE (exact expression) with B10-imaginary numbers
omega=2*np.pi*1
delta= np.sqrt(2/(omega*mu_0*mu_r*sigma)) 
gamma=((1+1j)/delta)
e=(1/(3*(b**3)*(gamma**2)*mu_r))
h=((3*b)-big_delta)
k=((a*b*(gamma**2)-1))
l=(((a**2)*(b**2)*(gamma**2))+(b**2)-(a*big_delta))
o=(gamma*big_delta)
SE_ee=(np.abs((e*((2*big_delta*(mu_r**2))+mu_r*((a*b*h*\
(gamma**2))-big_delta)+(big_delta*k))*np.cosh(o))+((e*\
((gamma**2)*l)+(h*big_delta*mu_r*(gamma**2))+(2*k*\
(mu_r**2))+mu_r+1)*np.sinh(o))))                

print("SE exact expression=", SE_ee)




# graphing SE_ts vs f
f=np.logspace(0, 5, 500) 
omega=2*np.pi*f 
delta= np.sqrt(2/(omega*mu_0*mu_r*sigma))  
SE_ts=(r_0/(3*math.sqrt(2)*mu_r*delta))*((np.exp(big_delta/delta)))
SE_ts_db= 20*np.log10(SE_ts)   
print()

fig=plt.figure()
ax=fig.add_subplot()
ax.plot(f, SE_ts_db)
ax.set_xscale('log')

ax.set_xlabel("frequency in Hz")
ax.set_ylabel("SE in dB")
ax.set_title("SE thick shield")

ax.grid(True, which="both", ls="--", color='0.65')

plt.show()




# graphing SE_ee vs f
f=np.logspace(0, 5, 500) 
omega=2*np.pi*f 
delta= np.sqrt(2/(omega*mu_0*mu_r*sigma)) 
gamma=(1+1j)/delta
e=(1/(3*(b**3)*(gamma**2)*mu_r))
h=((3*b)-big_delta)
k=((a*b*(gamma**2)-1))
l=(((a**2)*(b**2)*(gamma**2))+(b**2)-(a*big_delta))
o=(gamma*big_delta)                    
SE_ee=(np.abs((e*((2*big_delta*(mu_r**2))+mu_r*((a*b*h*\
(gamma**2))-big_delta)+(big_delta*k))*np.cosh(o))+((e*\
((gamma**2)*l)+(h*big_delta*mu_r*(gamma**2))+(2*k*\
(mu_r**2))+mu_r+1)*np.sinh(o))))    
                                                 
SE_ee_db= 20*np.log10(SE_ee)  
print()

fig=plt.figure()
ax=fig.add_subplot()
ax.plot(f, SE_ee_db)
ax.set_xscale('log')

ax.set_xlabel("frequency in Hz")
ax.set_ylabel("SE in dB")
ax.set_title("SE exact expression")

ax.grid(True, which="both", ls="--", color='0.65')

plt.show()




#graohing SE_ee and SE_ts vs f
f=np.logspace(0, 5, 500)
omega=2*np.pi*f
delta=np.sqrt(2/(omega*mu_0*mu_r*sigma))
SE_ts=(r_0/(3*math.sqrt(2)*mu_r*delta))*((np.exp(big_delta/delta)))
SE_ts_db=20*np.log10(SE_ts)  

gamma=(1+1j)/delta
e=(1/(3*(b**3)*(gamma**2)*mu_r))
h=((3*b)-big_delta)
k=((a*b*(gamma**2)-1))
l=(((a**2)*(b**2)*(gamma**2))+(b**2)-(a*big_delta))
o=(gamma*big_delta)                    
SE_ee=(np.abs((e*((2*big_delta*(mu_r**2))+mu_r*((a*b*h*\
(gamma**2))-big_delta)+(big_delta*k))*np.cosh(o))+((e*\
((gamma**2)*l)+(h*big_delta*mu_r*(gamma**2))+(2*k*\
(mu_r**2))+mu_r+1)*np.sinh(o))))                                                 
SE_ee_db= 20*np.log10(SE_ee)  

fig=plt.figure()
ax=fig.add_subplot()
ax.plot(f, SE_ts_db, label="thick shield")
ax.plot(f, SE_ee_db, label="exact expression")
ax.set_xscale('log')
ax.set_xlabel("frequency in Hz")
ax.set_ylabel("SE in dB")
ax.set_ylim(0, 85)
ax.grid(True, which="both", ls="--", color='0.65')
ax.legend()
plt.show()





