# https://leetcode.com/problems/delete-node-in-a-bst

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def list2tree2(nums):
    # 与我写的 list2tree 的区别是：对空值不再生成子节点，之后的数据也不会作为这个空节点的子节点，而是跳过，因此更加节省空间。
    if not nums:
        return None
    nodes = [None if val is None else TreeNode(val)
             for val in nums]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


class Solution:
    def searchBST(self, root, val):
        if root and val < root.val:
            return self.searchBST(root.left, val)
        elif root and val > root.val:
            return self.searchBST(root.right, val)
        return root

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            else:
                tmp, mini = root.right, root.right.val
                while tmp.left:
                    tmp, mini = tmp.left, tmp.left.val
                root.val = mini
                root.right = self.deleteNode(root.right, root.val)


a = list2tree2(nums=[5, 3, 6, 2, 4, None, 7])
key = 3
Solution().deleteNode(a, key)
