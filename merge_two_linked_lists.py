# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # We set the node to return and a dummy node to a blank node
        return_node = active_node = ListNode()

        # Looping through only while we have both leaves us an easy exit
        while l1 and l2:
            if l1.val <= l2.val:
                active_node.next = l1
                l1 = l1.next
            elif l2.val < l1.val:
                active_node.next = l2
                l2 = l2.next

            active_node = active_node.next

        # Because we know we only exit when one is empty we can pass the one
        # that isn't empty. If they're both empty it works even better
        active_node.next = l1 or l2

        return return_node.next
