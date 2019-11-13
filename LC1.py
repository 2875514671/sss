# -*- coding:utf-8 -*-
import random

nums = [10, 4, 2, 1, 6, 9, 5, 7, 13, 45, 33, 26, 19, 14, 22]
target = 20
# nums = [2, 7, 11, 15]
# target = 9
# nums = [3, 2, 4]
# target = 6


# def twoSum(nums, target):
#     for x in range(len(nums)):
#         for y in range(x + 1, len(nums)):
#             if nums[y] + nums[x] == target:
#                 print(x, y)
#                 return [x, y]
#     return []

def twoSum(nums, target):
    for x in range(len(nums)):
        y = target - nums[x]
        if y in nums[:x]:
            s = nums.index(y)
            print(x, s)
            return [x, s]
    return []


if __name__ == '__main__':
        twoSum(nums, target)
