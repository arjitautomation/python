list1=[1,4,5,7,2]
list2=[1,4,2,5,6]

def compare(list1,list2):
    
    comp=[]
    for i in range(0,len(list1)-1,1):
        for j in range(0,len(list2)-1,1):
            if list1[i]==list2[j]:
                comp.append(list1[i])
    print(comp)

compare(list1,list2)