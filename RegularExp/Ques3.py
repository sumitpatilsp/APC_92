import re
s = input("Enter a string: ")
result = re.findall(r'[aeiouAEIOU]', s)
print("Vowels:", len(result))