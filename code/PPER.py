factorial_cache = {}

def factorial(n):
    if n == 0 or n == 1:
        return 1
    if n not in factorial_cache:
        factorial_cache[n] = n * factorial(n - 1)
    return factorial_cache[n]

def partial_permutation(n, k):
    return factorial(n) // factorial(n - k)

n = int(input("Enter n: "))
k = int(input("Enter k: "))

print(partial_permutation(n, k) % 1000000)
