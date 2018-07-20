# https://leetcode.com/problems/move-zeroes
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        len_nums=len(nums)
        idx=0
        while idx<len_nums:
            if nums[idx]==0:
                nums.append(nums.pop(idx))
                len_nums-=1
            else:
                idx+=1



nums=[]
Solution().moveZeroes(nums)
print(nums)