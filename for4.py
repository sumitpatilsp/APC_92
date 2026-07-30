n = int(input("Enter n (exponent power): "))

print(f"Powers of 2 up to 2^{n}:")
for i in range(n + 1):
    print(2**i, end=" ")
print()