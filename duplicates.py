def unique(numbers):
    no=[]
    for n in numbers:
        if n not in no:
            no.append(n)
    print (no)

numbers=[1,2,3,4,5,6,7,8,1,2,4,5]
unique(numbers) 
