class Employee:
    def __init__(self, name):
        self.name = name


class Project:
    def __init__(self, employee):
        self.employ = employee


emp = Employee("Praveen")
project = Project(emp)
print(project.employ.name)