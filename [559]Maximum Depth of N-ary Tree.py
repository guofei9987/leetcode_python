# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

"""
# Definition for a Node.

"""

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root: return 0
        return max(self.maxDepth(i) for i in root.children+[None])+1


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return 0 if not root else max(self.maxDepth(i) for i in root.children+[None])+1
