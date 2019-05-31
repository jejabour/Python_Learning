import random

nums = list(range(1, 100))
random.shuffle(nums)
print(nums)

largest = nums[0]
print(largest)

for item in nums:
    if item > largest:
        largest = item
print (largest)