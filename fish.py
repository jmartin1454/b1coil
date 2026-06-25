# -*- coding: utf-8 -*-
"""
Created on Thu May 21 20:13:12 2026

@author: stimp
"""

class fish:
    def __init__ (self, colour="blue", age=12, name="marlon", kids=0):
        self.colour="blue"
        self.age=12
        self.name="marlon"
        self.kids=0
    def speak1(self):
            print("meow")
    def breathe(self):
            print("blub blub")
    def poop(self):
            print("plop")
    def get_caught(self): 
            print("RIP FISH. DIED AGE", self.age, "LOVED BY", self.kids, "CHILDREN")
    def age_up(self):
            self.age+=10 
    def reborn(self):
            self.age=0
    def reproduce(self): 
            self.kids+=15
 

f=fish(True)        
if f.age >= 18:
    print("marlon is an adult now!")
print ("what is your name?")
print (f.name)
print ("what colour are you?")
print (f.colour)
print ("how old are you?")
print (f.age)
if f.age >= 18:
     print("marlon is an adult now!") 
f.age_up()
print(f.age)
f.poop()
f.breathe()
f.reproduce()
f.get_caught()
f.reborn()
print(f.age)

f2=fish("orange","8", "bob",True)
if f.age >= 18:
    print(f2.name, "is an adult now!")





        