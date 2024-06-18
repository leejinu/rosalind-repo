"""
Problem: Introduction to Alternative splicing

Tip:
Understand the difference between the / and // operators

This problem calculates the total number of possible alternative splicing combinations
given the number of exons (n) and the minimum number of exons (m) in a gene.

"""

import math

def combination(n, r):
    # Calculate the combination using the formula nCr = n! / (r! * (n-r)!)
    return math.factorial(n) // (math.factorial(r) * math.factorial(n-r))

def calculate_alternative_splicing(n, m):
    # Initialize the result
    result = 0
    
    # Iterate from m to n (inclusive) and calculate the combination for each k
    for k in range(m, n+1):
        result += combination(n, k)
    
    # Return the result modulo 10^6 to avoid overflow
    return result % (10**6)

n = int(input("Enter the number of exons (n): "))
m = int(input("Enter the minimum number of exons (m): "))

print(calculate_alternative_splicing(n, m))
