def powerset_length(n):
    return 2 ** n % 10**6

n = int(input("Give total number of set: "))
print(powerset_length(n))

# Power set length: P(A)
# |P(A)| = 2**n
