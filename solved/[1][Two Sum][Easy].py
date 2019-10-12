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

#%%
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,num1 in enumerate(nums):
            if target-num1 in nums[i+1:]:
                return [i,i+nums[i+1:].index(target-num1)+1]


nums=[3,3]
target=6
Solution().twoSum(nums,target)
