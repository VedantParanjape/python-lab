x = [55,105,155,205,255,305,355,405,455]
y = [0.496, 0.645, 0.761, 0.867, 0.957, 1.037,1.113,1.194,1.254]

X = 0
Y = 0

for i in x:
    X = X + i
X = X/9

for j in y:
    Y = Y + j
Y = Y/9

def summation(val):
    sum = 0
    for i in val:
        sum = sum + i

    return sum

b1 = (summation(i*j for i,j in zip(x,y)) - summation(x)*summation(y)/9) / (summation(p**2 for p in x) - (summation(x)**2)/9)
b0 = Y-b1*X

print("b1: %8.6f"%(b1))
print("b0: %8.6f"%(b0))

print("| real  |   calc  |")

for i,j in zip(x,y):
    print("| {} | {} |".format(j, round(b0 + b1*i, 5)))