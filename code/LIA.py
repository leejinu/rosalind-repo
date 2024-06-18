"""
0th generation AaBb organisms -> 1
1th generation AaBb organisms -> 2
2th generation AaBb organisms -> 4
3th generation AaBb organisms -> 8
...
kth generation AaBb organisms -> 2**k

total organisms in the k th generation -> 4**k

the probability of having at least N organisms with AaBb
-> sum of 
"""
import math

def calculate_probability(k, N):
    # Calculate the number of organisms with genotype AaBb in the k-th generation
    organisms_with_AaBb = 2 ** k
    
    # Calculate the total number of organisms in the k-th generation
    total_organisms = 2 ** (2 * k)
    
    # Initialize the probability
    probability = 0
    
    # Calculate the probability of having at least N organisms with genotype AaBb
    for n in range(N, organisms_with_AaBb + 1):
        # Calculate the combination of organisms with genotype AaBb
        combinations = math.comb(organisms_with_AaBb, n)
        
        # Calculate the probability of having exactly n organisms with genotype AaBb
        probability += combinations * (0.25 ** n) * (0.75 ** (organisms_with_AaBb - n))
    
    return probability

# Sample Dataset
k, N = map(int, input().split())

# Calculate and print the probability
result = calculate_probability(k, N)
print(round(result,3))
