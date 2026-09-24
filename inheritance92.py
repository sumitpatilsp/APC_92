

# INHERITANCE - PROBLEM 1


def inheritance_1():
    class Employee:
        def __init__(self, emp_id, name, salary):
            self.emp_id = emp_id
            self.name = name
            self.salary = salary

        def display(self):
            print("Employee ID:", self.emp_id)
            print("Name:", self.name)
            print("Salary:", self.salary)

    class Manager(Employee):
        def __init__(self, emp_id, name, salary, department):
            super().__init__(emp_id, name, salary)
            self.department = department

        def annual_salary(self):
            return self.salary * 12

        def display(self):
            super().display()
            print("Department:", self.department)
            print("Annual Salary:", self.annual_salary())

    manager = Manager(101, "Rahul", 50000, "IT")
    manager.display()



# INHERITANCE - PROBLEM 2


def inheritance_2():
    class Vehicle:
        def __init__(self, brand, model):
            self.brand = brand
            self.model = model

        def display(self):
            print("Brand:", self.brand)
            print("Model:", self.model)

    class Car(Vehicle):
        def __init__(self, brand, model, fuel_type, price):
            super().__init__(brand, model)
            self.fuel_type = fuel_type
            self.price = price

        def discounted_price(self, discount):
            return self.price - (self.price * discount / 100)

        def display(self):
            super().display()
            print("Fuel Type:", self.fuel_type)
            print("Price:", self.price)

    car = Car("Toyota", "Camry", "Petrol", 3000000)
    car.display()
    print("Price after 10% discount:", car.discounted_price(10))


# INHERITANCE - PROBLEM 3


def inheritance_3():
    class Academic:
        def __init__(self, academic_marks):
            self.academic_marks = academic_marks

    class Sports:
        def __init__(self, sports_points):
            self.sports_points = sports_points

    class Student(Academic, Sports):
        def __init__(self, academic_marks, sports_points):
            Academic.__init__(self, academic_marks)
            Sports.__init__(self, sports_points)

        def overall_performance(self):
            return self.academic_marks + self.sports_points

        def display(self):
            print("Academic Marks:", self.academic_marks)
            print("Sports Points:", self.sports_points)
            print("Overall Performance:", self.overall_performance())

    student = Student(85, 15)
    student.display()


# INHERITANCE - PROBLEM 4


def inheritance_4():
    class PersonalDetails:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class ProfessionalDetails:
        def __init__(self, emp_id, designation, salary):
            self.emp_id = emp_id
            self.designation = designation
            self.salary = salary

    class Employee(PersonalDetails, ProfessionalDetails):
        def __init__(self, name, age, emp_id, designation, salary):
            PersonalDetails.__init__(self, name, age)
            ProfessionalDetails.__init__(
                self, emp_id, designation, salary
            )

        def display(self):
            print("Name:", self.name)
            print("Age:", self.age)
            print("Employee ID:", self.emp_id)
            print("Designation:", self.designation)
            print("Salary:", self.salary)

    employee = Employee(
        "Priya", 25, 1001, "Software Engineer", 60000
    )
    employee.display()

# INHERITANCE - PROBLEM 5


def inheritance_5():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Student(Person):
        def __init__(self, name, age, roll_no, course):
            super().__init__(name, age)
            self.roll_no = roll_no
            self.course = course

    class ResearchStudent(Student):
        def __init__(
            self, name, age, roll_no, course, research_topic, guide_name
        ):
            super().__init__(name, age, roll_no, course)
            self.research_topic = research_topic
            self.guide_name = guide_name

        def display(self):
            print("Name:", self.name)
            print("Age:", self.age)
            print("Roll No:", self.roll_no)
            print("Course:", self.course)
            print("Research Topic:", self.research_topic)
            print("Guide Name:", self.guide_name)

    student = ResearchStudent(
        "Amit",
        24,
        101,
        "M.Tech",
        "Artificial Intelligence",
        "Dr. Sharma"
    )
    student.display()


# INHERITANCE - PROBLEM 6


def inheritance_6():
    class BankAccount:
        def __init__(self, account_number, balance):
            self.account_number = account_number
            self.balance = balance

    class SavingsAccount(BankAccount):
        def __init__(self, account_number, balance, interest_rate):
            super().__init__(account_number, balance)
            self.interest_rate = interest_rate

        def calculate_interest(self):
            return self.balance * self.interest_rate / 100

    class PremiumSavingsAccount(SavingsAccount):
        def __init__(
            self, account_number, balance, interest_rate, benefits
        ):
            super().__init__(account_number, balance, interest_rate)
            self.benefits = benefits

        def display(self):
            print("Account Number:", self.account_number)
            print("Balance:", self.balance)
            print("Interest Rate:", self.interest_rate, "%")
            print("Interest:", self.calculate_interest())
            print("Benefits:", self.benefits)

    account = PremiumSavingsAccount(
        "SB1001", 100000, 7.5, "Free ATM, Airport Lounge"
    )
    account.display()

# INHERITANCE - PROBLEM 7


def inheritance_7():
    import math

    class Shape:
        def display_name(self):
            print("Shape")

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return math.pi * self.radius ** 2

    class Rectangle(Shape):
        def __init__(self, length, width):
            self.length = length
            self.width = width

        def area(self):
            return self.length * self.width

    class Triangle(Shape):
        def __init__(self, base, height):
            self.base = base
            self.height = height

        def area(self):
            return 0.5 * self.base * self.height

    circle = Circle(5)
    rectangle = Rectangle(10, 5)
    triangle = Triangle(8, 4)

    print("Circle Area:", circle.area())
    print("Rectangle Area:", rectangle.area())
    print("Triangle Area:", triangle.area())


# INHERITANCE - PROBLEM 8


def inheritance_8():
    class Employee:
        def __init__(self, emp_id, name, basic_salary):
            self.emp_id = emp_id
            self.name = name
            self.basic_salary = basic_salary

    class Manager(Employee):
        def calculate_salary(self):
            return self.basic_salary + self.basic_salary * 0.40

    class Developer(Employee):
        def calculate_salary(self):
            return self.basic_salary + self.basic_salary * 0.25

    class Tester(Employee):
        def calculate_salary(self):
            return self.basic_salary + self.basic_salary * 0.20

    employees = [
        Manager(1, "Manager", 50000),
        Developer(2, "Developer", 50000),
        Tester(3, "Tester", 50000)
    ]

    for employee in employees:
        print(
            employee.name,
            "Salary:",
            employee.calculate_salary()
        )


# INHERITANCE - PROBLEM 9

def inheritance_9():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Student(Person):
        def __init__(self, name, age, roll_no):
            super().__init__(name, age)
            self.roll_no = roll_no

    class Faculty(Person):
        def __init__(self, name, age, subject):
            super().__init__(name, age)
            self.subject = subject

    class TeachingAssistant(Student, Faculty):
        def __init__(self, name, age, roll_no, subject):
            Person.__init__(self, name, age)
            self.roll_no = roll_no
            self.subject = subject

        def display(self):
            print("Name:", self.name)
            print("Age:", self.age)
            print("Roll No:", self.roll_no)
            print("Subject:", self.subject)

    ta = TeachingAssistant("Neha", 23, 501, "Python")
    ta.display()



# INHERITANCE - PROBLEM 10


def inheritance_10():
    class Vehicle:
        def __init__(self, brand):
            self.brand = brand

        def display(self):
            print("Brand:", self.brand)

    class Car(Vehicle):
        def __init__(self, brand, model):
            super().__init__(brand)
            self.model = model

    class Bike(Vehicle):
        def __init__(self, brand, engine):
            super().__init__(brand)
            self.engine = engine

    class SportsCar(Car):
        def __init__(self, brand, model, top_speed):
            super().__init__(brand, model)
            self.top_speed = top_speed

        def display(self):
            print(
                "Sports Car:",
                self.brand,
                self.model,
                "Top Speed:",
                self.top_speed
            )

    class ElectricBike(Bike):
        def __init__(self, brand, engine, battery_capacity):
            super().__init__(brand, engine)
            self.battery_capacity = battery_capacity

        def display(self):
            print(
                "Electric Bike:",
                self.brand,
                "Battery:",
                self.battery_capacity
            )

    SportsCar("Ferrari", "F8", 340).display()
    ElectricBike("Ola", "Electric", "5 kWh").display()


# INHERITANCE - PROBLEM 11


def inheritance_11():
    class Student:
        def __init__(self, roll_no, name, course):
            self.roll_no = roll_no
            self.name = name
            self.course = course

    class Result(Student):
        def __init__(
            self, roll_no, name, course, mark1, mark2, mark3
        ):
            super().__init__(roll_no, name, course)
            self.mark1 = mark1
            self.mark2 = mark2
            self.mark3 = mark3

        def calculate(self):
            total = self.mark1 + self.mark2 + self.mark3
            percentage = total / 3

            if percentage >= 90:
                grade = "A"
            elif percentage >= 75:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "F"

            print("Total:", total)
            print("Percentage:", percentage)
            print("Grade:", grade)

    result = Result(101, "Riya", "BCA", 85, 90, 80)
    result.calculate()



# INHERITANCE - PROBLEM 12


def inheritance_12():
    class Product:
        def __init__(self, product_id, name, price):
            self.product_id = product_id
            self.name = name
            self.price = price

    class ElectronicProduct(Product):
        def __init__(
            self, product_id, name, price, brand, warranty
        ):
            super().__init__(product_id, name, price)
            self.brand = brand
            self.warranty = warranty

        def final_price(self, discount):
            return self.price - self.price * discount / 100

        def display(self):
            print("Product ID:", self.product_id)
            print("Name:", self.name)
            print("Brand:", self.brand)
            print("Warranty:", self.warranty)
            print("Final Price:", self.final_price(10))

    product = ElectronicProduct(
        101, "Laptop", 80000, "Dell", "2 Years"
    )
    product.display()



# INHERITANCE - PROBLEM 13


def inheritance_13():
    class Printer:
        def print_document(self, document):
            print("Printing:", document)

    class Scanner:
        def scan_document(self, document):
            print("Scanning:", document)

    class MultifunctionDevice(Printer, Scanner):
        pass

    device = MultifunctionDevice()
    device.print_document("Report.pdf")
    device.scan_document("Certificate.pdf")



# INHERITANCE - PROBLEM 14

def inheritance_14():
    class Camera:
        def take_photo(self):
            print("Photograph taken.")

    class Phone:
        def make_call(self, number):
            print("Calling:", number)

    class Smartphone(Camera, Phone):
        pass

    phone = Smartphone()
    phone.take_photo()
    phone.make_call("9876543210")



# INHERITANCE - PROBLEM 15


def inheritance_15():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Student(Person):
        def __init__(self, name, age, roll_no, course):
            super().__init__(name, age)
            self.roll_no = roll_no
            self.course = course

    class ResearchStudent(Student):
        def __init__(
            self,
            name,
            age,
            roll_no,
            course,
            research_topic,
            guide_name
        ):
            super().__init__(name, age, roll_no, course)
            self.research_topic = research_topic
            self.guide_name = guide_name

        def display(self):
            print("Name:", self.name)
            print("Age:", self.age)
            print("Roll No:", self.roll_no)
            print("Course:", self.course)
            print("Research Topic:", self.research_topic)
            print("Guide:", self.guide_name)

    student = ResearchStudent(
        "Kiran",
        25,
        202,
        "MCA",
        "Machine Learning",
        "Dr. Patil"
    )
    student.display()



# INHERITANCE - PROBLEM 16


def inheritance_16():
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

    class Student(Person):
        def __init__(self, name, age, roll_no, course):
            super().__init__(name, age)
            self.roll_no = roll_no
            self.course = course

    class ResearchStudent(Student):
        def __init__(
            self,
            name,
            age,
            roll_no,
            course,
            research_topic,
            guide_name
        ):
            super().__init__(name, age, roll_no, course)
            self.research_topic = research_topic
            self.guide_name = guide_name

        def display(self):
            print(
                self.name,
                self.age,
                self.roll_no,
                self.course,
                self.research_topic,
                self.guide_name
            )

    student = ResearchStudent(
        "Anita",
        26,
        303,
        "M.Sc",
        "Data Science",
        "Dr. Mehta"
    )
    student.display()



# INHERITANCE - PROBLEM 17


def inheritance_17():
    class Animal:
        def __init__(self, name):
            self.name = name

        def eat(self):
            print(self.name, "is eating.")

    class Dog(Animal):
        def sound(self):
            print(self.name, "says Woof!")

        def behavior(self):
            print(self.name, "is loyal.")

    class Cat(Animal):
        def sound(self):
            print(self.name, "says Meow!")

        def behavior(self):
            print(self.name, "is independent.")

    class Cow(Animal):
        def sound(self):
            print(self.name, "says Moo!")

        def behavior(self):
            print(self.name, "gives milk.")

    animals = [
        Dog("Bruno"),
        Cat("Kitty"),
        Cow("Ganga")
    ]

    for animal in animals:
        animal.eat()
        animal.sound()
        animal.behavior()



# INHERITANCE - PROBLEM 18


def inheritance_18():
    class Person:
        def __init__(self, name):
            self.name = name

    class Doctor(Person):
        def doctor_info(self):
            print(self.name, "is a doctor.")

    class Patient(Person):
        def patient_info(self):
            print(self.name, "is a patient.")

    class Surgeon(Doctor):
        def surgery(self):
            print(self.name, "performs surgery.")

    class MedicalResearcher(Doctor, Patient):
        def research(self):
            print(self.name, "conducts medical research.")

    surgeon = Surgeon("Dr. Ravi")
    researcher = MedicalResearcher("Dr. Priya")

    surgeon.doctor_info()
    surgeon.surgery()

    researcher.doctor_info()
    researcher.patient_info()
    researcher.research()

