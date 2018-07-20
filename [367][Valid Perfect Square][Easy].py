# https://leetcode.com/problems/valid-perfect-square
class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left,right=0,num
        while left<right:
            mid=(left+right)//2
            if mid*mid==num:
                return True
            elif mid*mid<num:
                left=mid+1
            elif mid*mid>num:
                right=mid-1
        if left*left==num:
            return True
        return False




for i in range(100):
    print(i,Solution().isPerfectSquare(i))
