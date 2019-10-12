# https://leetcode.com/problems/diagonal-traverse
class Solution:
    def findDiagonalOrder(self, matrix):
        l = [(i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))]
        l.sort(key=lambda x:100000*(x[0]+x[1])-x[(x[0]+x[1])%2])
        return [matrix[i][j] for (i,j) in l]