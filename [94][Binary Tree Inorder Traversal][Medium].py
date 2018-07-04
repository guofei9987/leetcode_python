# https://leetcode.com/problems/binary-tree-inorder-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.getInorder(root,inorder_list=[])
    def getInorder(self,root,inorder_list=[]):
        if root is not None:
            inorder_list=self.getInorder(root.left,inorder_list)
            inorder_list.append(root.val)
            inorder_list = self.getInorder(root.right, inorder_list)
        return inorder_list