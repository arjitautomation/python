class Employee:
    def __init__(self,name,age,location):
        self.name=name
        self.age=age
        self.location=location
        print(f"the name is {name} and age is {age} and he is staying at {location}")

#arjit=Employee("arjit","29","Utrecht")

class DevOps(Employee):
        def __init__(self):
             print(f"the name is")

        def __init__(self,skill):
             self.skill=skill
             print("The skill is DevOps")


arjit=DevOps("AWS")        