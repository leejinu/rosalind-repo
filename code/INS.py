def insertion_sort(arr):
    count = 0
    for i in range(1,len(arr)):
        k = i
        while k > 1 and arr[k] < arr[k-1]:
            temp = arr[k]
            arr[k] = arr[k-1]
            arr[k-1] = temp
            count +=1
            k = k-1
    return count

text = input()
numbers = text.split()
l = len(numbers)

A = [[0] for _ in range(0,l+1)]

for i, n in enumerate(numbers,1):
    A[i] = int(n)

print(A)

count= insertion_sort(A)

print(count)
        
