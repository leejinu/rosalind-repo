def fibonacci_modified(n, m):
    # Initialize an array to store the number of rabbit pairs for each month
    rabbits = [0] * (n+1)
    # Set the initial conditions
    rabbits[0] = 0
    rabbits[1] = 1
    
    for month in range(2, n+1):
        if month <= m:
            # If the month is within the lifespan of rabbits, use the standard Fibonacci formula
            rabbits[month] = rabbits[month-1] + rabbits[month-2]
        elif month == m + 1:
            # When rabbits start to die, subtract the number of rabbits that were born m months ago
            rabbits[month] = rabbits[month-1] + rabbits[month-2] - 1
        else:
            # After m months, rabbits are dying each month, so subtract the dying rabbits from the total
            rabbits[month] = rabbits[month-1] + rabbits[month-2] - rabbits[month-m-1]

    return rabbits[n]

# Example usage
n = 6
m = 3
result = fibonacci_modified(n, m)
print("Total number of pairs of rabbits after", n, "months if all rabbits live for", m, "months:", result)
