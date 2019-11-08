print("enter different rows separated by , on same line")
# matrix = input().split(',')
matrix = [i.split(' ') for i in input().split(',')]

transpose_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print(transpose_matrix)


#1 2 3
#4 5 6
#7 8 9

#1 4 7
#2 5 8
#3 6 9