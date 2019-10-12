# https://leetcode.com/problems/leaf-similar-trees/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def deserialize(self, string):
        # LeetCode官方版本
        # https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python
        # deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')
        # 这里是 deserialize 和 serialize 的案例
        # https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/995/discuss
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
    def findleaf_inorder(self, root):  # LDR
        if root is None:
            return []
        elif (root.left is None) and (root.right is None):
            return [root.val]
        else:
            return self.findleaf_inorder(root.left) + self.findleaf_inorder(root.right)

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.findleaf_inorder(root1) == self.findleaf_inorder(root2)


root1 = Solution1().deserialize('[18,35,22,null,103,43,101,58,null,97]')
root2 = Solution1().deserialize('[94,102,17,122,null,null,54,58,101,97]')

Solution().leafSimilar(root1, root2)

