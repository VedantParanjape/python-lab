option = int(input("1. enter a number \n2. enter a list \noption: "))

if option == 1:
    number = int(input("enter a number: "))

    if number%2 == 0:
        for i in range(number,0,-1):
            print (i, end = ' ')

    else:
        for i in range(0,number):
            print(i+1, end = ' ')
    
    print()

elif option == 2:
    number_list = [int(i) for i in input("enter a list of number: ").split(' ')]

    if len(number_list)%2 == 0:
        number_list.sort()
        print(number_list)

    else:
        number_list.sort(reverse=True)
        print(number_list)