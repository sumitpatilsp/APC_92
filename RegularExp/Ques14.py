import re
s = input("Enter text: ")
result =re.findall(r'https?://[^\s]+', s)
print("URLs:", result)