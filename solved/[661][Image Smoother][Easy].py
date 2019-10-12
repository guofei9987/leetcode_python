# https://leetcode.com/problems/image-smoother
import math


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """

        def smoother(M, i, j, row, col):
            sum_cells, count_cells = 0, 0
            for i1 in range(max(0, i-1), min(i+1, row-1)+1):
                for j1 in range(max(0, j-1), min(j+1, col-1)+1):
                    sum_cells += M[i1][j1]
                    count_cells += 1
            return sum_cells // count_cells

        row, col = len(M), len(M[0])
        return [[smoother(M,i,j,row,col) for j in range(col)] for i in range(row)]


M=[[1,1,1],
 [1,0,1],
 [1,1,1]]

M=[[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
Solution().imageSmoother(M)