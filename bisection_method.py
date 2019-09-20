import math
import matplotlib.pyplot as plt
def func(x):
    return math.exp(float(-x))*((3.2)*math.sin(float(x)) - (0.5)*math.cos(float(x)))

def bisection(a,b):

    if(func(a)*func(b) <= 0):
        c = a
        while(b-a >= 0.0000001):
            c = (a + b)/2
            print(c, func(c))
            plt.plot(c, func(c))
            plt.axis([a-b, a+b, -1, 1])
            plt.grid()
            plt.show()
            if func(c) == 0:
                break
            if func(a)*func(c) < 0:
                b = c
            else:
                a = c
        return c

a = int(input("enter a:"))
b = int(input("enter b:"))

def generateROOTS(a,b):
    ROOTval = []


def generateX(a,b):
    Xval = []

    while a<=b:
        a = a + 0.0001
        Xval.append(a)

    return Xval    

def generateY(a,b):
    Xlist = generateX(a,b)
    Yval = []

    for i in Xlist:
        Yval.append(func(i))

    return Yval

plt.plot(generateX(a,b),generateY(a,b))
plt.plot(bisection(a,b), 0, 'g^')
plt.axis([a-b, a+b, -1, 1])
plt.grid()
plt.show()