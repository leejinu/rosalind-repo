"""
3SUM Problem

Given a positive integer k ≤ 20, a positive integer n ≤ 10^4, and k arrays of size n containing integers from −10^5 to 10^5.

Return: For each array A[1..n], output three different indices 1 ≤ p < q < r ≤ n such that A[p] + A[q] + A[r] = 0 if exist, and "-1" otherwise.

"""

def read_file(path):
    # Read the file and extract k and n
    with open(path, 'r') as f:
        k, n = map(int, f.readline().split())
        # Read k arrays and store them in arrs
        arrs = [list(map(int, f.readline().split())) for _ in range(k)]
    return arrs, k, n

def find_pqr(A):
    # Sort the array A
    A.sort()
    # Loop to find p, q, and r
    for p in range(len(A) - 2):
        q, r = p + 1, len(A) - 1
        while q < r:
            # Check if A[p] + A[q] + A[r] = 0
            three_sum = A[p] + A[q] + A[r]
            if three_sum == 0:
                # Return p, q, and r
                return [p + 1, q + 1, r + 1]
            elif three_sum > 0:
                r -= 1
            else:
                q += 1
    # Return -1 if p, q, and r are not found
    return [-1]

def three_summation(arrs, k, n):
    # Call find_pqr for each array
    return [find_pqr(A) for A in arrs]

if __name__ == "__main__":
    arrs, k, n = read_file('../test/rosalind_3sum.txt')
    result = three_summation(arrs, k, n)
    # Write the result to output_3sum.txt
    with open('../result/output_3sum.txt', 'w') as f:
        for item in result:
            f.write(' '.join(map(str, item)) + '\n')
