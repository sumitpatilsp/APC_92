import re
s = input("Enter sentence: ")
result = re.findall(r'\b(\w+)\s+\1\b', s, re.IGNORECASE)
print("Repeated words:", result)