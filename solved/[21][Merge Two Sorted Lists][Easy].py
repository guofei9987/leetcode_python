# https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def should_put(self,node1,node2): # put node2 after node1
        if node1.next is None:
            return True
        if node2.val<=node1.next.val:
            return True
        return False

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1=l1
        node2=l2
        while node1:
            while node2:
                if self.should_put(node1,node2):
                    tmp1,tmp2=node1.next,node2.next
                    node1.next=node2
                    node2.next=tmp1
                    node2=tmp2
                else:
                    break
            node1=node1.next
        return l1 if l1 else l2



#%%

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 is None) or (l2 is None):return l1 or l2
        if l1.val<l2.val:
            l1.next=self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next=self.mergeTwoLists(l1,l2.next)
            return l2