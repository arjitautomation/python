secret=9
count=0
guess_limit=3
while count < guess_limit:
    num= int (input("Enter the number "))
    count=count+1
    remain= guess_limit-count
    print (str(remain) +" Remaining attempts")
    if num==secret:
        print("You guesses it correctly")
        break
else:
    print ("Sorry ! you failed")