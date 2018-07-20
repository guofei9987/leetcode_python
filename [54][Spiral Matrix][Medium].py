# https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and list(matrix.pop(0))+self.spiralOrder(list(zip(*matrix))[::-1])