# Vedant Paranjape 2019

# prints a alphabetic pyramid of user specified length

x = int(input("enter number of lines of pyramid: "))

for i in range(0,x):
    print(" "*(x-i-1), end = '')
    
    for j in range(65, 65+2*i+1):
        print(chr(65 + (j-65)%26), end = '')
    
    print('')

print(' ')
