class Employee:
    def __init__(self, name, skill, salary):
        self.name = name
        self.skill = skill
        self.salary = salary

    def role(self):
        print(f"{self.name} who is working on {self.skill} is getting the salary of {self.salary}")

Arjit = Employee("Arjit", "DevOps", 6000)
Arjit.role()

Sandeep=Employee("Sandeep","Java",7000)
Sandeep.role()
