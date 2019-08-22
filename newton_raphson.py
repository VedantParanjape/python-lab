def f(x):
    return float(int(x)**2 - 2)
def fp(x):
    return float(int(x)*2)

def newtonRaphson( x ): 
    h = f(x) / fp(x) 
    while abs(h) >= 0.000000000001: 
        h = f(x)/fp(x) 
          
        # x(i+1) = x(i) - f(x) / f'(x) 
        x = x - h 
        return x
  
 
x0 = float(input("enter x:")) 
print("solution: ", newtonRaphson(x0))
