# https://leetcode.com/problems/array-partition-i

class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[::2].sum()



nums=[1,32,3,2]
nums.sort()
sum(nums[::2])
