import re
s = input("Enter a sentence: ")
result = re.findall(r'\b[Aa]\w*', s)
print("Words:", result)