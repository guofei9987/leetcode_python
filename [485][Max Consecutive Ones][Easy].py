# https://leetcode.com/problems/max-consecutive-ones

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ones=0
        tmp_ones=0
        for i in nums:
            if i:
                tmp_ones+=1
            else:
                max_ones=max(tmp_ones,max_ones)
                tmp_ones=0
        max_ones=max(max_ones,tmp_ones)
        return max_ones

nums=[1,1,0,1,1,1]
# nums=[1,0,1,1,0,1]
s=Solution()
s.findMaxConsecutiveOnes(nums)