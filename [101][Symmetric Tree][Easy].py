# https://leetcode.com/problems/symmetric-tree
class TreeNode(object):
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


class Solution:
    def dlr(self, root):
        return [] if root is None else [root.val] + self.dlr(root.left) + self.dlr(root.right)

    def drl(self, root):
        return [] if root is None else [root.val] + self.drl(root.right) + self.drl(root.left)

    def ldr(self, root):
        return [] if root is None else self.ldr(root.left) + [root.val] + self.ldr(root.right)

    def rdl(self, root):
        return [] if root is None else self.rdl(root.right) + [root.val] + self.rdl(root.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 原理：前序遍历+中序遍历可以完全决定一个tree
        if not root:return True
        return (self.dlr(root.left)==self.drl(root.right)) and self.ldr(root.left)==self.rdl(root.right)


class Solution:
    def dlr(self, root):
        return [] if root is None else [root.val] + self.dlr(root.left) + self.dlr(root.right)

    def drl(self, root):
        return [] if root is None else [root.val] + self.drl(root.right) + self.drl(root.left)

    def ldr(self, root):
        return [] if root is None else self.ldr(root.left) + [root.val] + self.ldr(root.right)

    def rdl(self, root):
        return [] if root is None else self.rdl(root.right) + [root.val] + self.rdl(root.left)

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return True if not root else (self.dlr(root.left)==self.drl(root.right)) and self.ldr(root.left)==self.rdl(root.right)