from math import *

def f(x):
  return float(x**3 - 20)
 
def secant (x0, x1):
    e = 1
    counter = 0
    while (e >= 0.000001):
        e = abs(x1 - x0)/x1
        counter = counter + 1
        m = (f(x0)-f(x1))/(x0-x1)
        x0 = x1
        x1 = x1 - f(x1)/m
   
    print("number of iteration is: ", counter)
    print("error is: ", e)
    print("root is: ", x0)
         
                     
x0 = float(input("enter x0: "))
x1 = float(input("enter x1: "))                    
 
secant(x0,x1)