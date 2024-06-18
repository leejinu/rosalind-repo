"""
Problem: Maximum Matchings and RNA Secondary Structures

    Given: An RNA string s of length at most 100.

    Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s.
"""

import math

def nCr(n,r):
    if n<r:
        n, r = r, n
    return int(math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))

RNA_string = input("Enter RNA sequence: ")

A_indexes = []
U_indexes = []

G_indexes = []
C_indexes = []
for i, seq in enumerate(RNA_string):
    if seq == 'A':
        A_indexes.append(i)
    elif seq == 'U':
        U_indexes.append(i)
    elif seq == 'G':
        G_indexes.append(i)
    elif seq == 'C':
        C_indexes.append(i)

# Number of each kinds of RNA
A = len(A_indexes)
U = len(U_indexes)
G = len(G_indexes)
C = len(C_indexes)


if A > U:
    AU = U
else:
    AU = A

if G>C:
    GC = C
else:
    GC = G

print(math.factorial(AU)*nCr(A,U)*nCr(G,C)*math.factorial(GC))

