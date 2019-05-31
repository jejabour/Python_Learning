import random

nums = []

for q in range(100):
    x = random.randint(1, 30)
    nums.append(x)

nums.sort()

print(f'''
Original nums: {nums}
{len(nums)}
''')

dupe = nums[0]

for x in nums:
    dupe = x

    for y in nums[x:]:
        if dupe == y:
            nums.remove(y)

nums.sort()

print(f"Finished numbers {nums}")
print(len(nums))