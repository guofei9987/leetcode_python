# https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        list_num=self.getRow(rowIndex-1)
        print(len(list_num),rowIndex)
        for i in range(rowIndex-1):
            list_num[i]=list_num[i]+list_num[i+1]
        return [1]+list_num

s=Solution()
s.getRow(5)
