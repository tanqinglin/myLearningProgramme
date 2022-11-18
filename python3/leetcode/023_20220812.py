class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        if lists == []:
            return None
        
        p = result = ListNode()
        
        def findMin(lists):
            j = False
            for ln in lists:
                if ln != None:
                    if j == False:
                        min = ln.val
                        j = True
                    elif min > ln.val:
                        min = ln.val
            return None if not j else min
        
        min = findMin(lists)
        while min != None:
            for i in range(len(lists)):
                if lists[i] and min == lists[i].val:
                    p.next = ListNode(min, None)
                    p = p.next
                    lists[i] = lists[i].next
            min = findMin(lists)
        return result.next

if __name__ == '__main__':
    Test = Solution()
    print(Test.mergeKLists([ListNode(-1,ListNode(2,None)), ListNode(0,ListNode(1,None))]))