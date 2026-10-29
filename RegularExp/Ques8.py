import re
s = input("Enter a sentence: ")
result = re.findall(r'\b\w*s\b', s, re.IGNORECASE)
print("Words ending with s:", result)