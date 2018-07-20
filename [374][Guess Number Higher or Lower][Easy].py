# https://leetcode.com/problems/guess-number-higher-or-lower
def guess(x):
    true_num=10
    if true_num<x:
        return -1
    elif true_num>x:
        return 1
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

#%%
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left,right=0,n
        while left<right:
            mid=(left+right)//2
            if guess(mid)==-1:
                right=mid-1
            elif guess(mid)==1:
                left=mid+1
            else:
                return mid

        mid=left
        if guess(mid)==0:
            return mid
        else:
            return None


Solution().guessNumber(6)
