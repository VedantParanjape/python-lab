def f_x(y,z):
    return float((17-y+2*z)/20)

def f_y(x,z):
    return float((z-18-3*x)/20)

def f_z(x,y):
    return float((25-2*x+3*y)/20)

y0 = 0.0
z0 = 0.0


for i in range(20):
    x0 = f_x(y0,z0)
    y0 = f_y(x0,z0)
    z0 = f_z(x0,y0)

    print(x0,y0,z0)