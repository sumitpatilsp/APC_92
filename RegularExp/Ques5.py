import re
s = input("Enter text: ")
result = re.findall(r'[ \t\n]', s)
print("Spaces, tabs and newlines:", result)
print("Total:", len(result))