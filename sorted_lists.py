def sort_list(list, reverse=False):
    for i in range(0,len(list)):
        for j in range(0, len(list)-i-1):
            if list[j] > list[j+1] and not reverse:
                a = list[j]
                list[j] = list[j+1]
                list[j+1] = a

            elif list[j] < list[j+1] and reverse:
                a = list[j]
                list[j] = list[j+1]
                list[j+1] = a

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
        sort_list(number_list)
        print(number_list)

    else:
        sort_list(number_list, reverse=True)
        print(number_list)