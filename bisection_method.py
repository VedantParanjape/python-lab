import math

def func(x):
    return math.exp(float(-x))*((3.2)*math.sin(float(x)) - (0.5)*math.cos(float(x)))

def bisection(a,b):

    if(func(a)*func(b) <= 0):
        c = a
        while(b-a >= 0.0000001):
            c = (a + b)/2
            if func(c) == 0:
                break

            if func(a)*func(c) < 0:
                b = c
            else:
                a = c
            
        return c

a = int(input("enter a:"))
b = int(input("enter b:"))

print(bisection(a,b))