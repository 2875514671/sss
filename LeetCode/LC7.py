# -*- coding: utf-8 -*-


# 初始版本，38行，耗时32ms,内存占用11.7 MB
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        w = []
        l = len(str(x))
        if 0 < x and l < 2 ** 31:
            while l > 0:
                s = int(x % 10)
                x = x / 10
                l -= 1
                w.append(s)
            s = int(''.join(map(str, w)))
            if -2 ** 31 <= s <= 2**31 - 1:
                print(s)
            else:
                s = 0
                print(s)
            return s
        elif x < 0 and l > -2 ** 31:
            x = abs(x)
            l = l - 1
            while l > 0:
                s = int(x % 10)
                x = x / 10
                l -= 1
                w.append(s)
            s = int(''.join(map(str, w)))
            if -2 ** 31 <= s <= 2 ** 31 - 1:
                print(-s)
            else:
                s = 0
                print(s)
            return -s
        elif x == 0:
            return x


# 初次优化，25行，48ms,13.7MB，简直菜鸡,优化个毛
class Solution:
    def reverse(self, x: int) -> int:
        l = len(str(abs(x)))
        w = []
        while l > 0:
            if x < 0:
                i = int(x % -10)
            else:
                i = int(x % 10)
            x = x / 10
            l -= 1
            w.append(abs(i))
        s = int(''.join(map(str, w)))
        if -2 ** 31 <= s <= 2**31 - 1 and x > 0:
            print(s)
        elif -2 ** 31 <= s <= 2**31 - 1 and x < 0:
            s = -s
            print(s)
        elif x == 0:
            s = 0
            print(s)
        else:
            s = 0
            print(s)
        return s


# 二次优化，22行，48ms,14MB. 什么垃圾，菜鸡本鸡
class Solution:
    def reverse(self, x: int) -> int:
        l = len(str(abs(x)))
        w = []
        while l > 0:
            if x < 0:
                i = int(x % -10)
            else:
                i = int(x % 10)
            x = x / 10
            l -= 1
            w.append(abs(i))
        s = int(''.join(map(str, w)))
        if -2 ** 31 <= s <= 2**31 - 1 and x > 0:
            print(s)
        elif -2 ** 31 <= s <= 2**31 - 1 and x < 0:
            s = -s
            print(s)
        else:
            s = 0
            print(s)
        return s


"""
大佬版本,牛逼牛逼,8行,28ms,11.8MB
https://blog.csdn.net/qq_17550379/article/details/84666773
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = abs(x)
        s = str(l)[::-1]
        w = int(s)
        if w > pow(2, 31):
            w = 0
        return -w if x < 0 else w