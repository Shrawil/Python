# You are given all numbers between 1,2,..n except one.
# Your task is to find the missing number.

nums = [1,2,3,4]
n = 5

def solution(nums, n):
    nums = set(nums)
    mn = min(nums)
    for i in range(mn, n+1):
        if i not in nums:
            print(f"{i} is the missing number.")

solution(nums, n)