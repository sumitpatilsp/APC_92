t = (25, 10, 45, 5, 30, 60, 15)

largest = t[0]
smallest = t[0]

for n in t:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Largest:", largest)
print("Smallest:", smallest)