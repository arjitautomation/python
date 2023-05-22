def find_max(numbers):
    max= numbers[0]
    for n in numbers:
        if n > max:
            max= n
    return max    

numbers = [10,4,34,77,90]

x=find_max(numbers)
print(x)
print(max)
