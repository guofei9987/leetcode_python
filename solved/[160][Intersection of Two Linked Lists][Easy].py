# https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (headA is None) or (headB is None):
            return None
        pa,pb=headA,headB
        while True:
            if pa is pb:
                return pa
            else:
                pa=headB if pa is None else pa.next
                pb=headA if pb is None else pb.next
