
# . MATHUTILS PACKAGE

print("\n===== 7. MATHUTILS PACKAGE =====")

# basic.py functions
print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))

# number.py functions
n = 153

print("Prime:", prime(n))
print("Armstrong:", armstrong(n))
print("Palindrome:", number_palindrome(n))

# statistics.py functions
numbers = [10, 20, 30, 40, 50]

print("Mean:", sum(numbers) / len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))



# . STUDENT PACKAGE
# marks.py + grade.py + attendance.py


print("\n===== 8. STUDENT PACKAGE =====")

marks = [80, 85, 90, 75, 88]

total = sum(marks)
percentage = total / len(marks)

attendance = float(input("Enter attendance percentage: "))

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", student_grade(percentage))

if attendance >= 75:
    print("Attendance: Eligible")
else:
    print("Attendance: Not Eligible")



# . BANKING PACKAGE
# account.py + transaction.py + loan.py


print("\n===== 9. BANKING PACKAGE =====")

account = {
    "name": "Amit",
    "balance": 10000
}

print("Account Holder:", account["name"])
print("Initial Balance:", account["balance"])

# Deposit
deposit_amount = 5000
account["balance"] += deposit_amount

print("After Deposit:", account["balance"])

# Withdrawal
withdraw_amount = 2000

if withdraw_amount <= account["balance"]:
    account["balance"] -= withdraw_amount
    print("After Withdrawal:", account["balance"])
else:
    print("Insufficient Balance")

# Loan calculation
principal = 50000
rate = 8
years = 2

interest = principal * rate * years / 100
loan_amount = principal + interest

print("Loan Amount:", loan_amount)



# . TEXTTOOLS PACKAGE
# cleaning.py + tokenization.py + frequency.py


print("\n===== 10. TEXTTOOLS PACKAGE =====")

import string

text = input("Enter text: ")

# cleaning.py
clean_text = text.translate(
    str.maketrans("", "", string.punctuation)
)

clean_text = " ".join(clean_text.split())

# tokenization.py
words = clean_text.split()

# frequency.py
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("Clean Text:", clean_text)
print("Tokens:", words)
print("Word Frequency:", frequency)

