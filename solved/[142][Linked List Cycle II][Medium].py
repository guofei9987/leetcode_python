# https://leetcode.com/problems/linked-list-cycle-ii
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        fast=head
        slow=head
        while True:
            if (fast is None) or (slow is None):
                return None
            if (fast.next is None) or (fast.next.next is None) or (slow.next is None):
                return None
            fast=fast.next.next
            slow=slow.next
            if fast is slow:
                hooker = fast
                break
        fast=hooker
        slow=head
        while True:
            if fast is slow:
                return slow
            if fast is hooker:
                slow=slow.next
            fast=fast.next




# nums=[1,2,3,4,5]
# head=ListNode(nums[0])
# tmp=head
# for i in nums[1:]:
#     tmp.next=ListNode(i)
#     tmp=tmp.next
#
#
# tmp=head
# while tmp:
#     print(tmp.val)
#     tmp=tmp.next


#####################################################################
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        fast=head
        slow=head
        while True:
            if (fast is None) or (slow is None):
                return None
            if (fast.next is None) or (fast.next.next is None) or (slow.next is None):
                return None
            fast=fast.next.next
            slow=slow.next
            if fast is slow:
                break
        slow=head
        while True:
            if slow is fast:
                return fast
            else:
                slow=slow.next
                fast=fast.next




