# https://leetcode.com/problems/search-in-a-binary-search-tree/description/

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

a=list2tree2([4,2,7,1,3])


class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return []
        if root.val==val:
            return root
        elif root.val<val:
            return self.searchBST(root.right,val)
        elif root.val>val:
            return self.searchBST(root.left,val)

Solution().searchBST(root=a,val=2)