n = int(input())
items = input().split()
nums = list(map(lambda x : int(x), items))
prev = nums[0]
moves = 0
for i in range(1, n):
    if prev > nums[i]:
        moves += prev - nums[i]
        nums[i] = prev
    prev = nums[i]
print(moves)