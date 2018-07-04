# https://leetcode.com/problems/toeplitz-matrix
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        len_x,len_y=len(matrix),len(matrix[0])
        judge_dict=dict()
        for i in range(len_y):
            for j in range(len_x):
                if i-j not in judge_dict:
                    judge_dict[i-j]=matrix[j][i]
                elif matrix[j][i]!=judge_dict[i-j]:
                    return False
        return True

# guofei:a better solution
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for i in range(0,len(matrix)-1):
            if matrix[i][:-1] != matrix[i+1][1:]:
                return False
        return True