# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/


# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        level_order=[]
        deque=collections.deque([[root,0]])
        while deque:
            node,level=deque.popleft()
            if len(level_order)<=level:
                level_order+=[[]]*(level-len(level_order)+1)
            level_order[level].append(node.val)
            for i in node.children:
                deque.append([i,level+1])
        return level_order


#%%
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        nodes,nums=[root],[]
        while any(nodes):
            nums.append([node.val for node in nodes])
            nodes=[child for node in nodes for child in node.children if child]
        return nums
