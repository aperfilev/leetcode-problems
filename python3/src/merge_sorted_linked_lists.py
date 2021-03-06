class ListNode():
    val = None
    next = None
    
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution():
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        fake = ListNode(-1)
        last = fake
        
        while l1 and l2:
            if l1.value < l2.value:
                last.next = l1
                last = l1
                l1 = l1.next                    #time: O(N+M) space: O(1)
            else:
                last.next = l2
                last = l2
                l2 = l2.next
                
        if l1:
            last.next = l1
        if l2:
            last.next = l2
        
        return fake.next
    
        