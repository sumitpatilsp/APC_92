import re
s = input("Enter social media post: ")
result = re.findall(r'(?<!\w)#[A-Za-z0-9_]+', s)
print("Hashtags:", result)