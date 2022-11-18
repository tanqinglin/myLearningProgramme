# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None:
            return head
        
        p, p_last = head, None
        head = head.next

        while p != None and p.next != None:
            if p_last == None:
                p1 = p.next
                p.next = p1.next
                p1.next = p
                p_last = p
                p = p.next
            else:
                p1 = p.next
                p_last.next = p1
                p.next = p1.next
                p1.next = p
                p_last = p
                p = p.next

        return head


if __name__ == '__main__':
    Test = Solution()
    result = Test.swapPairs( ListNode(1, ListNode(2, ListNode(3, ListNode(4, None)))) )
    while result != None:
        print(result.val)
        result = result.next