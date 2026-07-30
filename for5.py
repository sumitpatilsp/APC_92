import math

n = int(input("Enter n: "))

# Initializing sum with 1 for the first term
total_sum = 1.0 

for i in range(1, n + 1):
    total_sum += 1 / math.factorial(i)

print(f"Sum of the sequence up to n={n} is: {total_sum}")