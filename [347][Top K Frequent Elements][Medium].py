# https://leetcode.com/problems/top-k-frequent-elements

def guess(num):
    right_num=6
    if num<right_num:
        return 1
    elif num>right_num:
        return -1
    else:
        return 0


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right=1,n
        while left<right:
            mid=(left+right)//2
            guess_num=guess(mid)
            if guess_num==0:
                return mid
            elif guess_num<0:
                right=mid-1
            else:left=mid+1
        return left


Solution().guessNumber(10)

