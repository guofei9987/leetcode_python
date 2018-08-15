# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        data_list=[]
        while head:
            data_list.append(head.val)
            head=head.next
        return data_list[len(data_list)//2:]


