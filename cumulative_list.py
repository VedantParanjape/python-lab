num_list = input("enter a list of numbers: ").split(' ')

sum = 0

for i in num_list:
    sum = sum + int(i)
    
    if sum > 0:
        print(i, end = ' ')

print()