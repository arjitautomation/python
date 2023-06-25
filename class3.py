class A:
    def feature1(self):
        print("feature 1 working from class A")

    def feature2(self):
        print("feature 2 working from class A")


class B(A):
        
    def feature3(self):
        print("feature 3 working from class B")

    def feature4(self):
        print("feature 4 working from class B")

a1=A()
a1.feature1()  
a1.feature2()

b1=B()
b1.feature4()
b1.feature1()