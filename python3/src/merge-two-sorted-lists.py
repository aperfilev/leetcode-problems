# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = ListNode()
        self.recMergeSort(l1, l2, output)
        return output.next

    def recMergeSort(self, l1: ListNode, l2: ListNode, out: ListNode): # O(len(l1) + len(l2))   S(len(l1) + len(l2))
        if not l1 and not l2:
            return

        out.next = ListNode()
        out = out.next

        if not l2:
            out.val = l1.val
            self.recMergeSort(l1.next, l2, out)
            return
        elif not l1:
            # l2 first
            out.val = l2.val
            self.recMergeSort(l1, l2.next, out)
            return

        if l1.val <= l2.val:
            # l1 first
            out.val = l1.val
            self.recMergeSort(l1.next, l2, out)
            return

        else:
            # l2 first
            out.val = l2.val
            self.recMergeSort(l1, l2.next, out)
            return