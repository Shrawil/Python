# Find the largest number (without max())

nums = [1,2,3,4,5,6,7]

m = nums[0]

for i in nums:
    if i > m:
        m = i

print(f"{m} is biggest {nums}.")