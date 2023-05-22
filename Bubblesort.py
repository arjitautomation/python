#Bubble Sort
def sort(nums):
    for i in range(len(nums)-1):
        for j in range(0, len(nums) - 1):
            if nums[j] > nums[j + 1]:
                # Swapping the elements using a temporary variable
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp

nums = [12, 4, 6, 18, 1,124]
sort(nums)

print(nums)
