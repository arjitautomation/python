string1 = ['a','r','j','i','t','a','r']
print("The original list is : " + str(string1))

# using naive method
# to remove duplicated
# from list
res = []
for i in string1:
    if i not in res:
        res.append(i)

    # printing list after removal
print("The list after removing duplicates : " + str(res))