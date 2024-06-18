filename = 'rosalind_maj.txt'
f = open(filename, 'r')

if f is False:
    print("Error: Check file existence.")
    print("Terminate the program.")
    exit()

text = f.read()

lines = text.split('\n')

arr = lines[0].split()

# k: number of arrays, n: size of each array
k = int(arr[0])
n = int(arr[1])

arr_2d = [[0]*n for _ in range(0, k)]

for i, line in enumerate(lines,0):
    if i == 0:
        continue
    if i == len(lines)-1:
        continue
    temp_list = line.split()
    print(len(temp_list))
    arr_2d[i-1] = temp_list.copy()


from collections import Counter

result = ""
for array in arr_2d:
    cnt = Counter(array)
    most_common = cnt.most_common(1)
    if int(most_common[0][1]) >= len(array)/2:
        result += most_common[0][0]
        result += " "
    else:
        result += "-1 "


print(result+"\b")

