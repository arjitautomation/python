nums=[7,9,1,4]
it=iter(nums)

print(it.__next__())
print(it.__next__())
print(it.__next__())
print(next(it))

for i in nums:
    print(i)