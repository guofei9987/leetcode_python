# https://leetcode.com/problems/power-of-two
import math

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a=math.log2(n)
        return int(a)==a


Solution().isPowerOfTwo(9)
# int(math.log(9,3))==math.log(9,3)

