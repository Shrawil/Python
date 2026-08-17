# You are given all numbers between 1,2,..n except one.
# Your task is to find the missing number.

n = int(input())
items = input().split()
nums = list(map(lambda x : int(x), items))

def solution(nums, n):
    nums = set(nums)
    for i in range(1, n+1):
        if i not in nums:
            print(i)

solution(nums, n)