# https://leetcode.com/problems/single-number-ii

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d=dict()
        for i in nums:
            if i in d:
                if d[i]==2:
                    d.pop(i)
                else:
                    d[i]+=1
            else:
                d[i]=1
        for i in d.keys():
            return i

nums=[2,2,3,2]
Solution().singleNumber(nums)