# https://leetcode.com/problems/two-sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        for i1 in range(n-1):
            for i2 in range(i1+1,n):
                if nums[i1]+nums[i2]==target:
                    return [i1,i2]