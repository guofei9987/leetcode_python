# https://leetcode.com/problems/remove-element

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        idx=0
        while idx<len(nums):
            if nums[idx]==val:
                nums.pop(idx)
            else:
                idx+=1
        return idx



s=Solution()
nums=[3,2,2,3]
val=3
nums=[0,1,2,2,3,0,4,2,3]
val=2
a=s.removeElement(nums,val)
print(nums[:a])