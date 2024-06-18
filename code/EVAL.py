"""
Expected Number of Restriction Sites
"""

import math
def prob_given_s(s, GC_content):
    AT = s.count('A') + s.count('T')
    GC = s.count('G') + s.count('C')
    prob = (((GC_content)/2)**GC)*(((1-GC_content)/2)**AT)

    return prob

def calculate_expected_counts(s, n, A):
    expected_counts = []
    m = len(s)

    for x in A:
        p = prob_given_s(s, x)

        expected_count = n-m+1
        expected_count *= p
        expected_counts.append(round(expected_count,3))
    return expected_counts
    
    
N = int(input("N: "))
s = input("s: ")
A = input("A: ")

A = [float(x) for x in A.split()]
print(A)
for x in calculate_expected_counts(s,N,A):
    print(x, end =' ')


