"""
Independent Segregation of Chromosome

Explanation:
This problem involves calculating the logarithm of the probability 
that two diploid siblings share at least k of their 2n chromosomes.
Each chromosome is inherited independently with a probability of 1/2,
which can be modeled using a binomial distribution.
Given an integer n, the task is to return an array of length 2n + 1.
Each element in the array represents the common logarithm of the probability 
that the siblings share at least k chromosomes.

Given: A positive integer n <= 50

Return: An array A of length 2n in which A[k] represents the common logarithm of
the probability that two diploid siblings share at least k of their 2n chromosomes (we do not consider recombination for now).

"""


def calculate_probabilities(n):
    A = []
    for k in range(1, 2 * n + 1):
        # Calculate cumulative probability
        cumulative_probability = sum(comb(2 * n, i) * ((0.5) ** (2 * n)) for i in range(k, 2 * n + 1))
        # Calculate common logarithm probability
        log_prob = round(math.log10(cumulative_probability), 3)
        # Format to 3 decimal places
        log_prob = "{:.3f}".format(log_prob)
        # Adjust for exact zero case
        if log_prob == "-0.000":
            log_prob = "0.000"
        A.append(log_prob)
    return A

# Function to calculate combinations
def comb(n, k):
    return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))

if __name__ == "__main__":
    import math
    # Example with n = 41
    n = 41
    results = calculate_probabilities(n)

    # Output the results
    result = ""
    
    for prob in results:
        result += prob+" "

    print(result)


