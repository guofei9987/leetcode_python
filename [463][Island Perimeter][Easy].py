# https://leetcode.com/problems/island-perimeter
class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        len_x=len(grid[0])
        len_y=len(grid)
        output=sum([sum(i) for i in grid])*4
        print(output)
        for i in range(len_x):
            for j in range(len_y):
                if grid[j][i]==1:
                    if i<len_x-1:
                        if grid[j][i+1]==1:
                            output-=2
                    if j<len_y-1:
                        if grid[j+1][i]==1:
                            output-=2
        return output
