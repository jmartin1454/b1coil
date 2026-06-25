# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:05:24 2026

@author: stimp
"""
import matplotlib.pyplot as plt
import math
from scipy.constants import mu_0, pi

class wire: 
    def __init__(self, xi, yi, i):
        self.xi = xi 
        self.yi = yi
        self.i = i
        print("wire created at (", self.xi, ",", self.yi, ")")
        print("the current of the wire is", self.i, "Amps")
        
    def move_to(self, new_xi, new_yi): 
        """moves the wire coords"""
        self.xi = new_xi
        self.yi = new_yi
        print("the coordinates of the wire have been moved to", "(", wr.xi,",", wr.yi, ")")
        
    def new_curr(self, new_i):
        """changes the current (still in Amps)"""
        self.i = new_i
        print("the current of the wire has been changed to", wr.i, "Amps")
        
   # def distance_from_origin(self):
   #     """calculates distance from (0,0).idk if i'll keep this..."""
   #     return math.hypot(self.xi, self.yi)
    
class point_of_interest: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("point of interest created at (", self.x, ",", self.y, ")")
        
    def move_to(self, new_x, new_y): 
        """moves the point of interest to new coords"""
        self.x = new_x 
        self.y = new_y 
        print("the point of interest has been moved to (", self.x, ",", self.y, ")")
        
    def rho(self, wire):
        """gives the distance from the wire to the point of interest"""
        rho = math.hypot((self.x - wire.xi), (self.y - wire.yi))
        print("rho is", rho)
        return rho
    
    def b(self, wire): 
        """gives the magnetic field at point of interest"""
        b = ((mu_0)*(wire.i))/((2*pi)*(math.sqrt(((self.x - wire.xi)**2) + ((self.y - wire.yi)**2))))
        print("b at point of interest is", b)
        return b 
        
    def bx(self, wire):
        """gives the x component of b"""
        alpha = math.atan(abs(self.y - wire.yi)/abs(self.x - wire.xi))
        print("alpha is", alpha, "radians")
        theta = pi/2 - alpha 
        print("theta is", theta, "radians")
        bx = ((mu_0)*(wire.i))/((2*pi)*(math.sqrt(((self.x - wire.xi)**2) + ((self.y - wire.yi)**2))))*math.cos(theta)
        print("x component of b at point of interest is", bx)
        return bx
    
    def by(self, wire): 
        """gives the y component of b"""
        alpha = math.atan(abs(self.y - wire.yi)/abs(self.x - wire.xi))
        theta = pi/2 - alpha 
        by = ((mu_0)*(wire.i))/((2*pi)*(math.sqrt(((self.x - wire.xi)**2) + ((self.y - wire.yi)**2))))*math.sin(theta)
        print("y component of b at point of interest is", by)
        return by
 
class cylinder: 
    def 
   
    
# this is where you define the location of the wire 
# wr is the short form of wire  
# wr = wire (xi coordinate, yi coordinate, current in Amp)
wr = wire(3, 5, 2)


# this is where you define the location of the point of interest
# p is the short form of point of interst
# p = point of interest (x coordinate, y coordinate)
p = point_of_interest(6, 1)
p.rho(wr)
p.b(wr)
p.bx(wr)
p.by(wr)




