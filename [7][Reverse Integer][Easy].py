# https://leetcode.com/problems/reverse-integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>2**31-1 or x<-2**31:
            return 0
        a=str(x)
        if a[0]=='-':
            sign='-'
            a=a[1:]
        else:sign=''
        y=int(sign+a[::-1])
        if y>2**31-1 or y<-2**31:
            return 0
        return int(y)