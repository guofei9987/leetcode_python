# https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.climbStairs(n-1)+self.climbStairs(n-2) if n>1 else 1


import math
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        sqrt_5=math.sqrt(5)
        fb= 1/sqrt_5*(((1+sqrt_5)/2)**(n+1)-((1-sqrt_5)/2)**(n+1))
        return round(fb)

Solution().climbStairs(2)