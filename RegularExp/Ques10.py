import re
s = input("Enter a sentence: ")
result = re.findall(r'\b\w+\b', s)
print("Number of words:", len(result))