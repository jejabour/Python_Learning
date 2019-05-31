#The objective here is to redo the largestnumber practice,
#  but with separate modules

from modules_practice_ext import find_max
import random

nums = list(range(1, 100))
random.shuffle(nums)

print(find_max(nums))