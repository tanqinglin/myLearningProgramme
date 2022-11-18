# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head, k):
        if head == None or head.next == None:
            return head
        p, l = head, 1
        
        while p.next != None:
            l += 1
            p = p.next
        k %= l
        if k == 0:
            return head

        p1 = p2 = head
        while k > 0:
            p2 = p2.next
            k -= 1
        
        while p2.next != None:
            p1 = p1.next
            p2 = p2.next
        
        p = p1.next
        p1.next = None
        p2.next = head
        return p

if __name__ == "__main__":
    Test = Solution()
    print(Test.rotateRight(head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None))))), k = 2))