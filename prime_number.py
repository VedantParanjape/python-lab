# Vedant Paranjape 2019

# prints if a number is prime or not

num = int(input("enter a number: "))

if num <= 0:
    print("enter valid number")

elif num%2 == 0 and num != 2:
    print("this is a non prime number")

else:
    flag = 1
    for i in range(2, int(num/2) + 1):

        if num%i == 0:
            flag = 0
            break
    
    if flag == 1:
        print("this is a prime number")
    else:
        print("this is a non prime number")
        
            