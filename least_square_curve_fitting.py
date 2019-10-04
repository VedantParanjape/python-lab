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

b1_n = 0
b1_d = 0

for i,j in zip(x,y):
    b1_n = b1_n + (i-X)*(j-Y)

for k in x:
    b1_d = b1_d + (k**2-X) 

b1 = b1_n/b1_d

print("b1: %8.6f"%(b1), sep = ' ')
print("b0: %8.6f"%(Y-b1*X), sep = ' ')