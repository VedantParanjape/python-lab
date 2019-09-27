def f(y,z):
    x = float((17-y+2*z)/20)
    y = float((z-18-3*x)/20)
    z = float((25-2*x+3*y)/20)
    
    return (x,y,z)

x0 = 0.0
y0 = 0.0
z0 = 0.0
count  = 0

while abs(float(20*x0+y0-2*z0-17))>0.00000000000000000000000001: 
    x0,y0,z0 = f(y0,z0)
    count = count + 1

print("<----------solution of the equations------------->")
print("x = {}".format(x0))
print("y = {}".format(y0))
print("z = {}".format(z0))
print("counter = {}".format(count))