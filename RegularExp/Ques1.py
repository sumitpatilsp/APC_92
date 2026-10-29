import re
s = input("Enter a string: ")
result = re.findall(r'\d', s)
print("Digits:", result)