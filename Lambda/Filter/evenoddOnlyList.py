nums = [10, 22, 45, 29, 92, 102, 43, 24]

evenNums = list(filter(lambda x : x % 2 == 0, nums))
oddNums = list(filter(lambda x : x % 2 != 0, nums))

print(evenNums)
print(oddNums)