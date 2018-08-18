# https://leetcode.com/problems/minimum-moves-to-equal-array-elements

class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_nums=min(nums)
        return sum([i-min_nums for i in nums])