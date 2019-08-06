def reverse(s):
    return s[::-1]


def isPalindrome(s):
    # Calling reverse function
    rev = reverse(s)

    # Checking if both string are equal or not
    if (s == rev):
        return True
    return False


# Driver code
s = input('Enter the string ')
ans = isPalindrome(s)

if ans == 1:
    print("Yes")
    total=len(s)
    if(total%2==0):
        print('it is a luck palindrome')
    else:
        print("it is not a luck palindrome because the string length is ",total)
else:
    print("No")