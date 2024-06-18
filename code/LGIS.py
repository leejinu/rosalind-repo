"""
Problem
A subsequence of a permutation is a collection of elements of the permutation in the order that
they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

A subsequence is increasing if the elements of the subsequence increase,
and decreasing if the elements decrease. For example,given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9),
an increasing subsequence is (2, 6, 7, 9),and a decreasing subsequence is (8, 6, 5, 4, 3).
You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
"""
def longest_increasing_subsequence(arr):
# length of given sequence
    n = len(arr)
# list of increasing sequence
    lis = [1] * n

    prev = [-1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1
                prev[i] = j

    max_length = max(lis)
    idx = lis.index(max_length)
    lis_sequence = []
    while idx != -1:
        lis_sequence.append(arr[idx])
        idx = prev[idx]

    return lis_sequence[::-1]

def longest_decreasing_subsequence(arr):
    n = len(arr)
    lds = [1] * n
    prev = [-1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] < arr[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1
                prev[i] = j

    max_length = max(lds)
    idx = lds.index(max_length)
    lds_sequence = []
    while idx != -1:
        lds_sequence.append(arr[idx])
        idx = prev[idx]

    return lds_sequence[::-1]

# Main body
def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')

    n = int(lines[0])
    arr = list(map(int, lines[1].split()))
    return arr

arr = read_file('rosalind_lgis.txt')

# Find longest increasing subsequence
lis_sequence = longest_increasing_subsequence(arr)

# Find longest decreasing subsequence
lds_sequence = longest_decreasing_subsequence(arr)

for n in lis_sequence:
    print(n, end= ' ')
print()
for n in lds_sequence:
    print(n, end= ' ')
