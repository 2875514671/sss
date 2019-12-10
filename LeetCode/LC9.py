# -*- coding: utf-8 -*-


class Solution:
    def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)[::-1]
        print(s)
        return s


if __name__ == '__main__':
    Solution.reverse(x=543)
