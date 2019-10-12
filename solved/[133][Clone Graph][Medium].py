# https://leetcode.com/problems/clone-graph

# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        stack=[node]
        while stack:
            v=stack.pop()
            for w in v.neighbors:
                if w note in
            stack.append()
