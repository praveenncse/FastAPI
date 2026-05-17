import copy
'''class Employee:
    def __init__(self,name,position,salary):
        self.name = name
        self.position = position
        self.salary = salary


    def show_detials(self):
        print(f"Name: {self.name }")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")

emp1 = Employee("Praveen", "Software Engineer", 10000)
emp2=copy.copy(emp1)
emp2.name = "John"
emp2.position = "Data Scientist"

emp1.show_detials()
print("\n")
emp2.show_detials() '''


###################################################################################################################

class Vehicle:
    def __init__(self,brand,color,model,price):
        self.brand = brand
        self.color = color
        self.model = model
        self.price = price

    def show_details(self):
        print(f"Brand: {self.brand}")
        print(f"Color: {self.color}")
        print(f"Model: {self.model}")
        print(f"Price: {self.price}")


vehicle1 = Vehicle(
    "Tesla",
    "Model S",
    "Black",
    90000
)
vehicle2 = copy.copy(vehicle1)
vehicle2.color = "White"
vehicle2.price = 95000

vehicle1.show_details()
print("\n")
vehicle2.show_details() 