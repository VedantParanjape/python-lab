row=3
col=3
print("Given matrix:")
a=[[1,23,3],[4,5,6],[7,8,9]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end="   ")
    print()
print()

def main(a):
    ac=a
    minors=[[0,0,0],[0,0,0],[0,0,0]]
    cof=[[0,0,0],[0,0,0],[0,0,0]]
    adj=[[0,0,0],[0,0,0],[0,0,0]]
    inv=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(a)):
        tempr=ac[i]
        del ac[i]

        for j in range(3):
            tempc1=ac[0][j]
            tempc2=ac[1][j]
            del ac[0][j]
            del ac[1][j]
            minors[i][j]=det(ac)
           
            ac[0].insert(j,tempc1)
            ac[1].insert(j,tempc2)


        ac.insert(i,tempr)

    for i in range(len(minors)):
        for j in range(len(minors[0])):
            if((i+j)%2!=0):
                cof[i][j]=(-1)*minors[i][j]
            else:
                cof[i][j]=minors[i][j]
    adj=transpose(cof)

    d=a[0][0]*minors[0][0]-a[0][1]*minors[0][1]+a[0][2]*minors[0][2]
    if(d==0):
        print("Inverse not possible")
        return
   

    for i in range(3):
        for j in range(3):
            inv[i][j]=round(adj[i][j]/d,3)

    print("Inverted matrix:")
    for i in range(len(inv)):
        for j in range(len(inv[i])):
            print(inv[i][j], end="   ")
        print()
    print()

def det(x):
    var=x[0][0]*x[1][1]-x[0][1]*x[1][0]
    return var

def transpose(M):
     T=[[0,0,0],[0,0,0],[0,0,0]]
     for i in range(len(M)):
         for j in range(len(M[0])):
             T[j][i]=M[i][j]
     return T

main(a)