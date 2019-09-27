import array

def bubble_sort(arr):
    for j in range(len(arr)-1):
        for i in range(len(arr)-1):
            if (arr[i] > arr[i+1]):
                a = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = a

n = int(input("enter number of elements to sort: "))
arr = array.array('i', [])

for i in range(n):
    arr.append(int(input("enter {} element: ".format(i))))

bubble_sort(arr)
print(arr)