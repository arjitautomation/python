def fact(num):
    fact=1
    for i in range(1,num+1,1):
        fact*=i
    print(fact)



num=int(input("Enter the number whose factorial needs to be found "))
if __name__=="__main__":
    fact(num)