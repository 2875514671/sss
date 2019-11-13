# -*- coding:utf-8 -*-
import random

"""
大佬牛逼
https://blog.csdn.net/qq_17550379/article/details/80435039
"""

nums = [10, 4, 2, 1, 6, 9, 5, 7, 13, 45, 33, 26, 19, 14, 22]
target = 20
# nums = [2, 7, 11, 15]
# target = 9
# nums = [3, 2, 4]
# target = 6


# 暴力破解法
def twoSum(nums, target):
    for x in range(len(nums)):
        for y in range(x + 1, len(nums)):
            if nums[y] + nums[x] == target:
                print(x, y)
                return [x, y]
    return []


# 一次循环，避免空表
def twoSum(nums, target):
    for x in range(len(nums)):
        y = target - nums[x]
        if y in nums[:x]:
            s = nums.index(y)
            print(x, s)
            return [x, s]
    return []


# 大佬的哈希算法，膜拜膜拜
def twoSum(nums, target):
    nums_hash = {}
    for x in range(len(nums)):
        y = target - nums[x]
        if y in nums_hash:
            s = nums_hash[y]
            print(x, s)
            return [x, s]
        nums_hash[nums[x]] = x
    return []


if __name__ == '__main__':
    twoSum(nums, target)
