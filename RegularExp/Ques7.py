import re
s = input("Enter a sentence: ")
result = re.findall(r'\b[A-Za-z]{5}\b', s)
print("Five-character words:", result)