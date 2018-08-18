# https://leetcode.com/problems/minimum-absolute-difference-in-bst

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def in_order(self,node):
        return self.in_order(node.left)+[node.val]+self.in_order(node.right) if node else []

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        inorder=self.in_order(root)
        for i in range(len(inorder)-1):
            inorder[i]=inorder[i+1]-inorder[i]
        inorder.pop()
        return min(inorder)
