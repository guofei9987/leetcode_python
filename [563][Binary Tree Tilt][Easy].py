# https://leetcode.com/problems/binary-tree-tilt

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sum_subtree(self,node):
        return self.sum_subtree(node.left)+self.sum_subtree(node.right)+node.val if node else 0

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findTilt(root.left) + self.findTilt(root.right) + \
               abs(self.sum_subtree(root.right) - self.sum_subtree(root.left)) if root else 0
