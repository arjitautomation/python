def dupl(str):
    name=[]
    for i in range(0,len(str)-1,1):
        if str[i] not in name:
            name.append(str[i])
    print (name)

str="Arjit Srivastava"
dupl(str)
