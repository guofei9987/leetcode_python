# https://leetcode.com/problems/same-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder(self,node):
        return self.inorder(node.left)+[node.val]+self.inorder(node.right) if node else [None]

    def preorder(self,node):
        return [node.val]+self.preorder(node.left)+self.preorder(node.right) if node else [None]

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return (self.inorder(p)==self.inorder(q)) and (self.preorder(p)==self.preorder(q))