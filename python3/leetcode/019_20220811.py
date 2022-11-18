# -*- coding:utf-8 -*-
# Definition for singly-linked list.

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        p1 = p2 = head
        p1_last = p2_last = None
        while n - 1 > 0:
            if p1.next == None:
                return []
            else:
                p1_last = p1
                p1 = p1.next
                n -= 1
        while p1.next != None:
            p1_last = p1
            p1 = p1.next
            p2_last = p2
            p2 = p2.next
        if p2_last != None:
            p2_last.next = p2.next
        else:
            return head.next
        return head

if __name__ == '__main__':
    Test = Solution()
    # p1 = ListNode(1, None)
    # print(Test.removeNthFromEnd(head, n))