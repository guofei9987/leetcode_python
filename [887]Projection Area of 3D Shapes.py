# https://leetcode.com/problems/projection-area-of-3d-shapes/description/

class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        shadow_xoy = sum([1 for i in grid for j in i if j != 0])
        shadow_xoz = sum([max(i) for i in grid])
        shadow_yoz = sum([max(i) for i in list(zip(*grid))])
        return shadow_xoy + shadow_xoz + shadow_yoz


grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
grid=[[2,2,2],[2,1,2],[2,2,2]]
grid=[[1,0],[0,2]]
# import numpy as np
#
# grid = np.array(grid)
#
# shadow_xoy=np.sum(grid==1)


shadow_xoy=sum([1 for i in grid for j in i if j!=0])
shadow_xoz=sum([max(i) for i in grid])
shadow_yoz=sum([max(i) for i in list(zip(*grid))])
shadow_xoy+shadow_xoz+shadow_yoz

