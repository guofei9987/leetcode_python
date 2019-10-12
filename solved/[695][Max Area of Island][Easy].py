# https://leetcode.com/problems/max-area-of-island

class Solution:
    def find_joint_island(self):
        island = self.stack.pop()
        i, j = island
        for x in (i - 1, i + 1):
            if 0 <= x < self.row:
                if self.grid[x][j] == 1:
                    self.stack.append([x, j])
                    self.area += 1
                    self.grid[x][j] = -1
        for y in (j - 1, j + 1):
            if 0 <= y < self.col:
                if self.grid[i][y] == 1:
                    self.stack.append([i, y])
                    self.area += 1
                    self.grid[i][y] = -1

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.row, self.col = len(grid), len(grid[0])
        max_area = 0
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == 1:
                    self.stack = [[i, j]]
                    self.grid[i][j]=-1
                    self.area = 1
                    while self.stack:
                        self.find_joint_island()
                    max_area = max(max_area, self.area)
        return max_area


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

# grid=[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
Solution().maxAreaOfIsland(grid)

#%%

class Solution:
    def dfs(self,i,j):
        if (0<=i<self.row) and (0<= j<self.col) and(grid[i][j]==1):
            self.grid[i][j]=-1
            return 1+self.dfs(i-1,j)+self.dfs(i+1,j)+self.dfs(i,j-1)+self.dfs(i,j+1)
        return 0
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid=grid
        self.row,self.col=len(grid),len(grid[0])
        area=[self.dfs(i,j) for i in range(self.row) for j in range(self.col)]
        return max(area) if area else 0