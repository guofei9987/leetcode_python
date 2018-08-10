# https://leetcode.com/problems/remove-nth-node-from-end-of-list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l=0
        p=head
        while p is not None:
            l+=1
            p=p.next
        p=head
        if l==n:
            return p.next
        for i in range(l-n-1):
            p=p.next
        p.next=p.next.next
        return head



