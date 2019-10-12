# https://leetcode.com/problems/search-for-a-range

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return -1,-1
        left_range, right_range = -1, -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid - 1
        mid = left
        if nums[mid] == target:
            left_range=mid
        else:
            if mid + 1 <= len(nums) - 1:
                if nums[mid+1]==target:
                    left_range=mid+1

        left,right=left_range,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<=target:
                left=mid+1
        mid=left
        if nums[mid]==target:
            right_range=mid
        else:
            if mid-1>=0:
                if nums[mid-1]==target:
                    right_range=mid-1
        return left_range,right_range


nums = [1,2,3]
target = 2
Solution().searchRange(nums,target)

