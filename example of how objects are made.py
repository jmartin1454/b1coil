# -*- coding: utf-8 -*-
"""
Created on Thu May 21 13:48:24 2026

@author: stimp
"""

class cat:
    def __init__(self,colour="orange", age=10):
        self.colour=colour
        self.age=age
    def speak1(self):
        print("meow")
    def speak2(self):
        print("meeeow")
    def get_older(self):
        self.age+=1
        
        
        
        
c=cat()
print(c.colour)
c.speak1()
print (c.age)
c.get_older()
print(c.age)
c.speak2()



c2=cat("blue")
print(c2.age)
print(c2.colour)
c.speak2()
