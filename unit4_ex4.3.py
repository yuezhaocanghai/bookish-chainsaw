#练习4.3-1
import turtle
bob = turtle.Turtle()

def square(t):
    for i in range(4):
        bob.fd(100)
        bob.lt(90)
    turle.mainloop()
    
print(square(bob))
      
#练习4.3-2
import turtle
bob = turtle.Turtle()

def square(t,length):
    for i in range(4):
        bob.fd(length)
        bob.lt(90)
    turle.mainloop()
    
print(square(bob,60))

#练习4.3-3
import turtle
bob = turtle.Turtle()

def polygon(t,n,length):
    for i in range(n):
        bob.fd(length)
        bob.lt(360/n)
    turle.mainloop()
    
print(polygon(bob,3,60))

#练习4.3-4
import turtle
bob = turtle.Turtle()

def polygon(t,n,length):
    for i in range(n):
        bob.fd(length)
        bob.lt(360/n)
    turle.mainloop()
    
import math
def circle(t,r):
    circumeference = math.pi * 2 * r
    n = 100
    length = circumference / n
    polygon(t,n,length)
    
print(circle(bob,50))


