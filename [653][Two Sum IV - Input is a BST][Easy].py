# https://leetcode.com/problems/two-sum-iv-input-is-a-bst
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def InOrder(self,root):
        return self.InOrder(root.left)+[root.val]+self.InOrder(root.right) if root else []

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        InOrder=self.InOrder(root)
        while InOrder:
            i=InOrder.pop()
            if k-i in InOrder:
                return True
        return False
