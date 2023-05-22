class student():
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print(self.name, self.rollno) 

s1=student ("Navin",2)
s1.show()
