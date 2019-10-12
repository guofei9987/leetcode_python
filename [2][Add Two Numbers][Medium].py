# https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        l3 = ListNode(None)
        zero = ListNode(0)
        curr1, curr2, curr3 = l1, l2, l3

        while True:
            if (curr1 is None) and (curr2 is None) and (carry == 0):
                break

            add_value = (curr1.val if curr1 else 0) + (curr2.val if curr2 else 0) + carry
            carry, val = divmod(add_value, 10)
            curr3.next = ListNode(val)
            curr3 = curr3.next
            curr1 = curr1.next if curr1 else curr1
            curr2 = curr2.next if curr2 else curr2
        return l3.next
