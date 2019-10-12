# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right=0,len(nums)-1
        if left==right:return nums[0]
        if nums[left]<nums[right]:return nums[left]
        while left<right:
            mid=(left+right)//2
            if nums[mid]>=nums[left]:
                if nums[mid]>nums[mid+1]:
                    return nums[mid+1]
                else:left=mid+1
            elif nums[mid]<nums[-1]:
                right=mid-1
        return nums[left+1]


nums=[3,4,5,1,2]
# nums=[4,5,6,7,0,1,2]
# nums=[1]
# nums=[2,1]
nums=[1,2]
nums=[4,5,1,2,3]
Solution().findMin(nums)