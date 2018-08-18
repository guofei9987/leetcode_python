# https://leetcode.com/problems/power-of-four

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:return False
        a=math.log(num,4)
        return 4**round(a)==num
