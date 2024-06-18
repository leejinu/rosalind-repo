from numba import jit

@jit(nopython=True)
def merge(A, B):
    merged_arr = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged_arr.append(A[i])
            i += 1
        else:
            merged_arr.append(B[j])
            j += 1
    while i < len(A):
        merged_arr.append(A[i])
        i += 1
    while j < len(B):
        merged_arr.append(B[j])
        j += 1
    return merged_arr

filename = '/content/gdrive/MyDrive/rosalind/rosalind_mer.txt'

with open(filename, 'r') as f:
    lines = f.read().split('\n')

A = list(map(int, lines[1].split()))
B = list(map(int, lines[3].split()))

merged_result = merge(A, B)

# Print the merged array
for num in merged_result:
    print(num, end=" ")
