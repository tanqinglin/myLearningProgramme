# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        
        if list1 == None:
            return list2
        
        if list2 == None:
            return list1

        if list1.val < list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        p = head

        while list1 != None or list2 != None:
            if list1 == None:
                p.next = list2
                list2 = None
            elif list2 == None:
                p.next = list1
                list1 = None
            else:
                if list1.val < list2.val:
                    p.next = list1
                    p, list1 = p.next, list1.next
                else:
                    p.next = list2
                    p, list2 = p.next, list2.next
        
        return head

if __name__ == '__main__':
    Test = Solution()
    Test.mergeTwoLists()
        