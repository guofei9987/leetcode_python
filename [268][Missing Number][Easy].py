# https://leetcode.com/problems/missing-number

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(range(len(nums)+1))-sum(nums)