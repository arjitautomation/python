class Person:
    name= "Arjit"
    Age=87
    role= "software engineer"
    def intro(self):
        print(f"{self.name} is {self.role}")

anshika = Person()

anshika.name ="Cute"
anshika.intro()
print(anshika.name)