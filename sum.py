def addition(num):
    numstr=str(num)
    length=len(numstr)
    sum=0
    for i in range(0,length):
        sum=sum + int (numstr[i])
    print (sum)    

num=int(input("Enter a number: "))

def find_max(numbers):
    max= numbers[0]
    for n in numbers:
        if n > max:
            max= n
    return max    

numbers = [10,4,34,77,90]

if __name__== "__main__":
    addition(num)
    print (find_max(numbers))
