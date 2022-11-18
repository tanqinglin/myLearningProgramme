# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        if k == 1:
            return head
        
        n, nonHead = head, 1

        while True:
            
            i = 1
            left = right = n
            if n == None:
                return head
            
            while i < k:
                right = right.next
                i += 1
                if right == None:
                    p.next = n
                    return head

            n = right.next
            tail = left
            right.next = None
            sub = None

            while left != None:
                right = left.next
                left.next = sub
                sub = left
                left = right
            
            if nonHead:
                head = sub
                nonHead = 0
                p = tail
            else:
                p.next = sub
                p = tail
            

if __name__ == '__main__':
    Test = Solution()
    result = Test.reverseKGroup( ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, None)))))), 3 )
    while result != None:
        print(result.val)
        result = result.next