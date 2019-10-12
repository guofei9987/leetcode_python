# https://leetcode.com/problems/binary-tree-level-order-traversal-ii

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:return []
        res=[]
        nodes,values=[root],[root.val]
        while nodes:
            res.append([node.val for node in nodes])
            tmp=[]
            for node in nodes:
                if node.left:tmp.append(node.left)
                if node.right:tmp.append(node.right)
            nodes=tmp
        return res[::-1]


