# Two Sum

def twoSum(self, nums, target):
    ans = {}

    for i, num in enumerate(nums):
        temp = target - num
        if temp in ans:
            return [ans[temp], i]
        ans[num] = i
    return []
