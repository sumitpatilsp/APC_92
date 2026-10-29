import re
s = input("Enter a string: ")
result = re.sub(r'[^A-Za-z0-9 ]', '', s)
print("Result:", result)