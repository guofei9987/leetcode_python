# https://leetcode.com/problems/convert-bst-to-greater-tree

class Solution:
    def InOrder(self, root):
        return self.InOrder(root.left) + [root.val] + self.InOrder(root.right) if root else []

    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.inorder = self.InOrder(root)
        self.sum=0
        def rdl(node):
            if node:
                rdl(node.right)
                node.val+=self.sum
                self.sum=node.val
                rdl(node.left)
        rdl(root)
        return root