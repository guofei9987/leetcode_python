# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dlr(self,node):
        return [node.val]+self.dlr(node.left)+self.dlr(node.right) if node else []

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dlr_list=list(set(self.dlr(root)))
        dlr_list.sort()
        if len(dlr_list)>=2:
            return dlr_list[1]
        else:
            return -1
