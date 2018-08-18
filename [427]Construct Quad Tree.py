# https://leetcode.com/problems/construct-quad-tree/description/


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        if all([all([i == grid[0][0] for i in j]) for j in grid]):
            return Node(val=bool(grid[0][0]), isLeaf=True,
                        topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
        N = len(grid)
        node = Node(val=bool(grid[0][0]), isLeaf=False,
                    topLeft=self.construct([[grid[i][j] for j in range(N // 2)] for i in range(N // 2)]),
                    topRight=self.construct([[grid[i][j] for j in range(N // 2, N)] for i in range(N // 2)]),
                    bottomLeft=self.construct([[grid[i][j] for j in range(N // 2)] for i in range(N // 2, N)]),
                    bottomRight=self.construct([[grid[i][j] for j in range(N // 2, N)] for i in range(N // 2, N)])
                    )
        return node


class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        N = len(grid)
        return Node(val=bool(grid[0][0]), isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None) \
            if all([all([i == grid[0][0] for i in j]) for j in grid]) \
            else Node(val=bool(grid[0][0]), isLeaf=False,
                      topLeft=self.construct([[grid[i][j] for j in range(N // 2)] for i in range(N // 2)]),
                      topRight=self.construct([[grid[i][j] for j in range(N // 2, N)] for i in range(N // 2)]),
                      bottomLeft=self.construct([[grid[i][j] for j in range(N // 2)] for i in range(N // 2, N)]),
                      bottomRight=self.construct([[grid[i][j] for j in range(N // 2, N)] for i in range(N // 2, N)])
                      )


grid = [[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]

Solution().construct(grid)
