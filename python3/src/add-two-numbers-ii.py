# Definition for singly-linked list.
from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        node = self
        nodes = []
        while node:
            nodes.append(str(node.val))
            node = node.next

        return "".join(nodes)

def buildLinkedList(list : List):
    root = None
    if len(list) > 0:
        node = ListNode(list[0])
        root = node
    for i in range(1, len(list)):
        node.next = ListNode(list[i])
        node = node.next

    return root

def reverseList(node : ListNode):
    _node = None
    while node:
        _node = ListNode(node.val, _node)
        node = node.next

    return _node


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        listNode1 = reverseList(l1)
        listNode2 = reverseList(l2)

        node = ListNode(0)
        overDigit = 0
        while listNode1 or listNode2 or overDigit > 0:
            list1Val = listNode1.val if listNode1 else 0
            list2Val = listNode2.val if listNode2 else 0

            sum = list1Val + list2Val + overDigit

            node.val = sum % 10
            overDigit = int(sum / 10)

            listNode1 = listNode1.next if listNode1 else None
            listNode2 = listNode2.next if listNode2 else None

            if listNode1 or listNode2 or overDigit:
                node = ListNode(0, node)

        return node

print(Solution().addTwoNumbers(buildLinkedList([7, 2, 4, 3]), buildLinkedList([5, 6, 4])).print())
