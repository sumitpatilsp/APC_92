import re
s = input("Enter paragraph: ")
result = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', s)
print("Dates:", result)