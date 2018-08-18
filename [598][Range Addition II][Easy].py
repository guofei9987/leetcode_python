# https://leetcode.com/problems/range-addition-ii

class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:return m*n
        a,b=list(zip(*ops))
        return min(a)*min(b)
