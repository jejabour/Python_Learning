
#Apparently this is the very hard way to do it

# import random

# nums = list(range(1, 100))
# random.shuffle(nums)
# print(nums)

# largest = nums[0]
# print(largest)

# for item in nums:
#     if item > largest:
#         largest = item
# print (largest)


#Mosh did it like this
numbers = [10, 3, 6, 2]
max = numbers[0]
for number in numbers:
        if number > max:
                max = number
print(max)