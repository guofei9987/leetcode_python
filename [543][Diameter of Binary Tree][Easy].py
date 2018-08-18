# https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def get_depth(self, node):
        return max(self.get_depth(node.left), self.get_depth(node.right)) + 1 if node else 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.diameterOfBinaryTree(root.left),self.diameterOfBinaryTree(root.right),
                   self.get_depth(root.left)+self.get_depth(root.right)+1) if root else 0
