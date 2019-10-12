# https://leetcode.com/problems/target-sum


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(nums) == 0:
            if S==0:
                return 1
            else: return 0
        for i in nums:
            if i == 0:
                return 2 * self.findTargetSumWays(nums[1:], S)
            else:
                return self.findTargetSumWays(nums[1:], S - i) + self.findTargetSumWays(nums[1:], S + i)


# nums = [1, 0]
# S = 1
# nums =  [1, 1, 1, 1, 1]
# S = 3
nums = [20, 48, 33, 16, 19, 44, 14, 31, 42, 34, 38, 32, 27, 7, 22, 22, 48, 18, 48, 39]
S = 1
Solution().findTargetSumWays(nums, S)
