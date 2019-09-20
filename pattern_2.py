# Vedant Paranjape 2019

# prints
#      A
#     ABC
#    ABCDE
#   ABCDEFG

for i in range(0,4):
    print(" "*(4-i-1), end = '')
    
    for j in range(65, 65+2*i+1):
        print(chr(j), end = '')
    
    print('')

print(' ')
