# -*- coding: utf-8 -*-

# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l = ListNode(val = l1.val + l2.val, next = None)
        p = l
        p1 = l1
        p2 = l2
        c = l.val // 10
        l.val %= 10
        while p1.next != None or p2.next != None or c != 0:
            if p1.next != None:
                p1 = p1.next
                c += p1.val
            if p2.next != None:
                p2 = p2.next
                c += p2.val
            p.next = ListNode(c % 10, None)
            p = p.next
            c = c // 10
        return l

if __name__ == '__main__':
    l1 = ListNode(0, None)
    l2 = ListNode(0, None)
    A = Solution()
    A.addTwoNumbers(l1, l2)