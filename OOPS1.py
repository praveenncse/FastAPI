class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary
    
    def increase_salary(self,amount):

        if amount > 0 and amount <= (self.__salary * 0.5):
            self.__salary += amount
        else:
            print("Amount exceeds allowed limit.")

    def decrease_salary(self,amount):
        if amount > 0 and amount <= self.__salary:
            self.__salary -= amount
        else:
            print("Amount exceeds current salary.")

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary must be non-negative.")
    
    def display(self):
        print(f"Name: {self.name}, Salary: {self.__salary}")

emp = Employee("Praveen", 10000)

print(emp.get_salary())     # 50000

emp.increase_salary(6000)
print(emp.get_salary())     # 55000

emp.decrease_salary(60000)  # should not allow

emp.set_salary(-100)   
emp.display()            # Name: Praveen, Salary: 55000  