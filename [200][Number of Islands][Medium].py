# https://leetcode.com/problems/number-of-islands

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        total_row, total_col = len(grid), len(grid[0])
        count_ilands = 0
        for i in range(total_row):
            for j in range(total_col):
                if grid[i][j] == '1':
                    count_ilands += 1
                    self.dfs(grid,i,j)
        return count_ilands

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '2'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)
        self.dfs(grid, i, j + 1)


grid = [list('11110'),
        list('11010'),
        list('11000'),
        list('00000')]

grid = [["1", "1", "1"], ["0", "1", "0"], ["1", "1", "1"]]
Solution().numIslands(grid)
