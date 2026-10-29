import re
s = input("Enter paragraph: ")
result = re.findall(r'\b[1-9]\d{5}\b', s)
print("PIN codes:", result)