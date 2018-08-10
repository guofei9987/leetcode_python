# https://leetcode.com/problems/validate-binary-search-tree
class Solution:
    def inorder(self, root):  # LDR
        return [] if (root is None) else self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def preorder(self, root):  # DLR
        return [] if (root is None) else [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def postorder(self, root):  # LRD
        return [] if (root is None) else self.inorder(root.left) + self.inorder(root.right) + [root.val]

    def isValidBST(self,root):
        inorder=self.inorder(root)
        return inorder==list(sorted(set(inorder)))