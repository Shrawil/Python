# Second largest element

nums = [1,2,3,4,5,5,6,7,8]

l1 = nums[0]
l2 = nums[0]

for i in nums:
    if i > l1:
        l1 = i

for i in nums:
    if i > l2 and i < l1:
        l2 = i

print(l1,l2)