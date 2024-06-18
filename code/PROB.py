"""
Introduction to Random Strings

Given: A DNA string s of length at most 100 bp and an array A
 containing at most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k]
 represents the common logarithm of the probability that
 a random string constructed with the GC-content found in A[k] will match s exactly.
 """

import math

def read_file(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
    s = ""
    num = ""
    
    for line in lines:
        if line and line[0].isalpha() is True:
            s += line.strip()
        else:
            num += " "+line
    numbers = [float(x) for x in num.split()]

    return s, numbers
def log_pos_seq(nt, GC_contents):
    if nt == 'A' or nt == 'T':
        return math.log10((1-GC_contents)/2)
    elif nt == 'C' or nt == 'G':
        return math.log10(GC_contents/2)
    
def calculate_pos_seq(A,s):
    n = len(A)
    result = []

    for i in range(0, n):
        p = 0
        for nt in s:
            p += log_pos_seq(nt, A[i])
        result.append(p)
    return result
            
A = []
B = []


s, A = read_file('rosalind_prob.txt')

print(s)
print(A)

B = calculate_pos_seq(A, s)

for pos_log in B:
    print('{:.3f}'.format(round(pos_log, 3)), end = ' ')
