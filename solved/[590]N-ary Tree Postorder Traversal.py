# https://leetcode.com/problems/n-ary-tree-postorder-traversal/description/


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        return [] if not root else [j for i in root.children for j in self.postorder(i)] + [root.val]
