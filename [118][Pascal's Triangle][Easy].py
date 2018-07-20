# https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        list_output = [[1] * i for i in range(1, numRows + 1)]

        print(list_output)
        for i in range(1, numRows - 1):
            for j in range(i):
                list_output[i + 1][j + 1] = list_output[i][j] + list_output[i][j + 1]
        return list_output

s=Solution()
s.generate(5)
