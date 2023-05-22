try:
    age= int (input("Enter you age "))
    print(age)
    income= 2000
    risk= income/age
except ZeroDivisionError:
    print ("Age can not be 0")
except ValueError:
    print("Value error")    