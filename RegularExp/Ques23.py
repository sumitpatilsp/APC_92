import re
s = input("Enter Python code: ")
result = re.findall(r'#.*', s)
print("Comments:", result)