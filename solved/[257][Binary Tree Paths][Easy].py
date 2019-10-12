# https://leetcode.com/problems/binary-tree-paths


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:return []
        node_str = str(root.val)
        if (not root.left) and (not root.right): return [node_str]
        return [node_str + '->' + i for i in self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)]
