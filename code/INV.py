def getInvCount(arr, n):
 
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1
 
    return inv_count
 
 
with open('rosalind_inv.txt','r') as f:
    text = f.read()
    lines = text.split('\n')

n = int(lines[0])
arr = lines[1].split()

arr = [int(x) for x in arr]

print("Number of inversions are",
      getInvCount(arr, n))
