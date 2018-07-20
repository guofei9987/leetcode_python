# https://leetcode.com/problems/first-bad-version

def isBadVersion(version):
    if version>=1:
        return True
    else:return False



class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right=0,n
        if isBadVersion(0):return 0
        while left<right:
            mid=(left+right)//2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                else:right=mid-1
            else:left=mid+1
        return left


s=Solution()
s.firstBadVersion(1)


