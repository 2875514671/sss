# -*- coding: utf-8 -*-
"""
https://blog.csdn.net/qq_17550379/article/details/80435080  Leetcode 2:两数相加（最详细解决方案！！！）
"""


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype  : ListNode
        """
        cur = ret = ListNode(0)
        add = 0

        while l1 or l2 or add:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add
            add = val // 10
            cur.next = ListNode(val % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return ret.next
