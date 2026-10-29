import re
s = input("Enter invoice text: ")
invoice = re.findall(r'INV-\d+', s)
dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b', s)
amounts = re.findall(r'₹\s*\d+(?:,\d{3})*(?:\.\d{2})?', s)
print("Invoice numbers:", invoice)
print("Dates:", dates)
print("Amounts:", amounts)