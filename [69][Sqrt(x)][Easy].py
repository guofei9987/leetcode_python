# https://leetcode.com/problems/sqrtx

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<=1:return x
        left,right=0,x
        while left<right:
            mid=(left+right)//2
            if mid*mid<=x<(mid+1)*(mid+1):
                return mid
            elif x<mid*mid:
                right=mid
            else:
                left=mid+1



a=Solution().mySqrt(8)
print(a)

