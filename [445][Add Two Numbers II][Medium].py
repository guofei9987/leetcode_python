# https://leetcode.com/problems/add-two-numbers-ii

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = '', ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num = str(int(num1) + int(num2))
        l3 = ListNode(None)
        curr = l3
        for i in num:
            curr.next = ListNode(int(i))
            curr = curr.next

        return l3.next