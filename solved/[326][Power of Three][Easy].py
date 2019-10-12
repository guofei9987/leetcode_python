# https://leetcode.com/problems/power-of-three
import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:return False
        a=math.log(n,3)
        return 3**round(a)==n

# 177146
Solution().isPowerOfThree(19682)

# math.log(,3)


# class Solution(object):
#     def isPowerOfThree(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         if n<=0:return False
#         a=math.log(n,3)
#         return abs(round(a)-a)<0.01