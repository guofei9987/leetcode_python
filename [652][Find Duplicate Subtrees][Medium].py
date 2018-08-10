# https://leetcode.com/problems/find-duplicate-subtrees

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def trv(root):
            if not root: return "null"
            struct = "%s,%s,%s" % (str(root.val), trv(root.left), trv(root.right))
            nodes[struct].append(root)
            return struct

        # nodes = collections.defaultdict(list)
        nodes=dict()
        trv(root)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]

import collections
collections.defaultdict(list)
a=collections.defaultdict()
a.default_factory=123
