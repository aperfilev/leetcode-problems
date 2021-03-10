# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = ListNode()
        self.recAddition(l1, l2, output, 0)
        return output

    def recAddition(self, l1: ListNode, l2: ListNode, out: ListNode, upperValue):

        digitSum = l1.val + l2.val + upperValue

        out.val = digitSum % 10
        upperValue = int(digitSum / 10)

        if l1.next or l2.next or upperValue > 0:
            out.next = ListNode()

            if not l1.next:
                l1.next = ListNode()

            if not l2.next:
                l2.next = ListNode()

            self.recAddition(l1.next, l2.next, out.next, upperValue)


