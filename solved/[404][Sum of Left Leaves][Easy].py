# https://leetcode.com/problems/sum-of-left-leaves

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left:
            if (root.left.left is None) and (root.left.right is None):
                return root.left.val+self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)