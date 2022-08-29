# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Just making things strings and flipping and adding them
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = str(l1.val)
        num2 = str(l2.val)

        while l1.next or l2.next:
            if l1.next:
                l1 = l1.next
                num1 = num1 + str(l1.val)
            if l2.next:
                l2 = l2.next
                num2 = num2 + str(l2.val)

        num3 = str(int(num1[::-1]) + int(num2[::-1]))[::-1]

        dummy = cur = ListNode('#')

        for i in num3:
            cur.next = ListNode(i)
            cur = cur.next

        return dummy.next
