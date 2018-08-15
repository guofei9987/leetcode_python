# https://leetcode.com/problems/average-of-levels-in-binary-tree


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        dict_value=dict()
        import collections
        deque = collections.deque((root, 0))
        while deque:
            node,level = deque.popleft(deque)
            if node.left: deque.append(node.left)
            if node.right: deque.append(node.right)
            node