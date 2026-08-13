prices = (100, 250, 150, 500, 300)

total = sum(prices)
average = total / len(prices)

print("Total bill:", total)
print("Average price:", average)
print("Highest-priced item:", max(prices))
print("Lowest-priced item:", min(prices))