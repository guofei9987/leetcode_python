# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(3)

l2=ListNode(1)
l2.next=ListNode(3)
l2.next.next=ListNode(4)

tmp_node1=l1
tmp_node2=l2
# while (tmp_node1 is not None) and (tmp_node2 is not None):
#     tmp=l1.next

def func(l1,l2):
    if l1.val<l2.val
        merged_lists=