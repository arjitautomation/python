list=[1,2,3,4,5,6,9,1,2,3]
print('The list is ', list)
res=[]
res1=[]
for i in list:
    if i not in res:
        res.append(i)
    else:
        res1.append(i)

print('the result is ',str(res))
print('the duplicate numbers are',str(res1))