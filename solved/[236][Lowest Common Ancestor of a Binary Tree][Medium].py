# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def PrintTree(self, root, i=0):
        '''
        打印二叉树，凹入表示法。原理是RDL遍历，旋转90度看
        '''
        tree_str = ''
        if root.right:
            tree_str += self.PrintTree(root.right, i + 1)
        if root.val:
            tree_str += ('    ' * i + '-' * 3 + str(root.val) + '\n')
        if root.left:
            tree_str += self.PrintTree(root.left, i + 1)
        return tree_str

    def deserialize(self, string):
        # LeetCode官方版本
        # deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')
        if string == '{}':
            return None
        nodes = [None if val == 'null' else TreeNode(int(val)) for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root in (None,p,q):return root
        left,right=[self.lowestCommonAncestor(kid,p,q) for kid in (root.left,root.right)]
        return root if left and right else left or right