# Create a class Student with attributes
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def percentage(self):
        return sum(self.marks) / len(self.marks)
    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", self.percentage())

students = [
    Student(1, "Amit", [80, 75, 90, 85, 70]),
    Student(2, "Riya", [85, 88, 92, 78, 90]),
    Student(3, "Rahul", [70, 65, 80, 75, 72])
]
for student in students:
    student.display()
    print()
    
#Create a class Employee with attributes
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def hra(self):
        return self.basic_salary * 0.20

    def da(self):
        return self.basic_salary * 0.10

    def gross_salary(self):
        return self.basic_salary + self.hra() + self.da()

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.hra())
        print("DA:", self.da())
        print("Gross Salary:", self.gross_salary())


emp = Employee(101, "Amit", 30000)
emp.display()

#Create a class Rectangle with attributes 
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r = Rectangle(10, 5)

print("Area:", r.area())
print("Perimeter:", r.perimeter())

#Create a class Circle with an attribute 
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius


c = Circle(7)

print("Area:", c.area())
print("Circumference:", c.circumference())

#Create a class Book containing book_id, title, author, and price
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)


books = [
    Book(1, "Python Basics", "John", 500),
    Book(2, "Data Science", "Smith", 700),
    Book(3, "Machine Learning", "David", 900)
]

for book in books:
    book.display()
    print()
    
    #Create a class ElectricityBill containing consumer number
    
    class ElectricityBill:
     def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        units = self.units

        if units <= 100:
            bill = units * 1.5
        elif units <= 200:
            bill = 100 * 1.5 + (units - 100) * 2.5
        elif units <= 500:
            bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
        else:
            bill = 100 * 1.5 + 100 * 2.5 + 300 * 4 + (units - 500) * 6

        return bill

    def display(self):
        print("Consumer No:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units:", self.units)
        print("Bill:", self.calculate_bill())


bill = ElectricityBill(1001, "Amit", 350)
bill.display()

#Create a class MobilePhone with attributes brand, model
class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specs(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price:", self.price)

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)


phone = MobilePhone("Samsung", "S24", "256GB", 70000)

phone.display_specs()
print("Price after discount:", phone.discounted_price(10))

#Create a class Patient containing patient ID, name
class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def total_bill(self, medicine_fee):
        return self.consultation_fee + medicine_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)


p = Patient(101, "Rahul", 25, "Fever", 500)

p.display()
print("Total Bill:", p.total_bill(800))

#Design an ATM class that allows a user to:

class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance")

    def display_account(self):
        print("Account No:", self.account_no)
        print("Name:", self.name)
        print("Balance:", self.balance)


atm = ATM(10001, "Amit", 10000)

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Account Details")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        atm.check_balance()
    elif choice == 2:
        amount = float(input("Enter amount: "))
        atm.deposit(amount)
    elif choice == 3:
        amount = float(input("Enter amount: "))
        atm.withdraw(amount)
    elif choice == 4:
        atm.display_account()
    elif choice == 5:
        print("Thank you")
        break
    else:
        print("Invalid choice")
        
        #Create a class Vehicle containing vehicle number
        class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate, availability=True):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.availability = availability

    def rent(self):
        if self.availability:
            self.availability = False
            print("Vehicle rented successfully")
        else:
            print("Vehicle is not available")

    def return_vehicle(self, days):
        if not self.availability:
            self.availability = True
            print("Rental charge:", self.rental_rate * days)
        else:
            print("Vehicle is already available")


vehicle = Vehicle("MH12AB1234", "Swift", 1000)

vehicle.rent()
vehicle.return_vehicle(3)

#Create a class ShoppingCart with customer name and cart ID.
class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = {}

    def add_product(self, name, price):
        self.products[name] = price

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]

    def total_bill(self):
        return sum(self.products.values())

    def display(self):
        print("Customer:", self.customer_name)
        print("Cart ID:", self.cart_id)
        print("Products:", self.products)
        print("Total Bill:", self.total_bill())

    def __del__(self):
        print("Shopping cart destroyed")


cart = ShoppingCart("Amit", 101)

cart.add_product("Laptop", 50000)
cart.add_product("Mouse", 1000)
cart.add_product("Keyboard", 2000)

cart.remove_product("Mouse")
cart.display()

del cart

#Create a class FoodOrder with order ID, customer name
class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        amount = self.quantity * self.price
        tax = amount * 0.05
        return amount + tax

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Total Bill:", self.total_bill())

    def __del__(self):
        print("Order completed")


order = FoodOrder(101, "Riya", "Pizza", 2, 300)

order.display()

del order

#Create a class StudentResult with student name 
class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Name:", self.name)
        print("Total:", self.total())
        print("Percentage:", self.percentage())
        print("Grade:", self.grade())

    def __del__(self):
        print("Student result object destroyed")


student = StudentResult("Amit", [85, 90, 78, 88, 92])

student.display()

del student