import re
s = input("Enter a sentence: ")
result = re.sub(r' +', ' ', s)
print("Result:", result)