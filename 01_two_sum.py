# Two Sum - Hashing
nums = [2, 7, 11, 15]
target = 9

seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        print([seen[complement], i])
        break
    seen[num] = i
