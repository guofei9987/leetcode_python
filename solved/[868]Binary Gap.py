# https://leetcode.com/problems/binary-gap/description/

class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        max_gap=0
        gap=0
        for i in bin(N)[2:]:
            if i=='1':
                max_gap=max(gap,max_gap)
                gap=1
            else:
                gap+=1
        return max_gap


Solution().binaryGap(8)
