# https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd,even=head,head.next
        podd,peven=odd,even
        idx=0
        while True:
            peven.next=podd.next
            podd.next=podd.next.next
            peven=peven.next
            podd=podd.next
        podd.next=even









