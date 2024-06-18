"""
2SUM Problem

Given a set of integers, find two elements that add up to 0.

Input:
The first line of the input file contains two integers, k and n.
The next k lines contain n integers each, representing k sets of integers.

Output:
For each set of integers, output the indices of two elements that add up to 0, separated by a space.
If no such pair is found, output -1.

Example:
Input:
2 3
-1 0 1
-2 2 3
Output:
2 3
-1
"""

def read_file(path):
    # Open the file and read the first line to get k and n
    with open(path, 'r') as f:
        k, n = map(int, f.readline().split())
        # Read the rest of the lines and store them in A
        A = [list(map(int, line.split())) for line in f.readlines()]
    return k, n, A

def find_two_sum(arr):
    # Find the indices of two numbers in the array that add up to 0
    for i, num in enumerate(arr):
        for j in range(i + 1, len(arr)):
            if num + arr[j] == 0:
                # Return the indices (add 1 because indices start at 1)
                return [i + 1, j + 1]
    # If no such pair is found, return -1
    return [-1]

def solve(k, n, A):
    # For each array in A, find the indices of two numbers that add up to 0
    for arr in A:
        result = find_two_sum(arr)
        # Print the result with spaces in between
        print(' '.join(map(str, result)))

if __name__ == "__main__":
    # Read the file and initialize k, n, and A
    k, n, A = read_file('../test/rosalind_2sum.txt')
    # Solve the problem
    solve(k, n, A)
