from random import *

nums = [1,2,3]

print(random())
print(randint(1,10))
print(randrange(1,10,2))
print(uniform(1,10))
print(choice(nums))
#print(choices(population, weights, k))
print(choices(nums, weights=[10,1,1], k=2))
print(sample([1,2,3,4], 2))
shuffle(nums)
print(nums)