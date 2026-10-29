import re
s = input("Enter filenames: ")
result = re.findall(r'\.([A-Za-z0-9]+)\b', s)
print("File extensions:", result)