# https://leetcode.com/problems/average-of-levels-in-binary-tree


class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        dict_value = dict()
        import collections
        deque = collections.deque([[root, 0]])
        while deque:
            node, level = deque.popleft()
            if node.left: deque.append((node.left, level + 1))
            if node.right: deque.append((node.right, level + 1))
            if not level in dict_value:dict_value[level]=[0,0]
            dict_value[level][0] += node.val
            dict_value[level][1] += 1
        return [dict_value[i][0] /dict_value[i][1] for i in dict_value]