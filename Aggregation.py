class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self,employees):
        self.employees = employees

emp1 = Employee("Praveen")
emp2= Employee("John")
Department1 = Department([emp1, emp2])