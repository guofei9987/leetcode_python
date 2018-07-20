# encoding=utf-8
# https://leetcode.com/problems/search-in-rotated-sorted-array


class Solution:
    def find_sorted(self, nums, target, left, right):
        if (left == right) and (nums[left] == target):
            return left
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def find_pivot(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                if nums[mid + 1] > nums[-1]:
                    left = mid + 1
                else:
                    return mid
            elif nums[mid] < nums[-1]:
                right = mid - 1
        return left

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == []: return -1
        if nums[0] <= nums[-1]: return self.find_sorted(nums, target, 0, len(nums) - 1)
        pivot_point = self.find_pivot(nums)
        if target >= nums[0]:
            return self.find_sorted(nums, target, 0, pivot_point)
        else:
            return self.find_sorted(nums, target, pivot_point + 1, len(nums) - 1)


s = Solution()
nums = [6, 7, 1, 2, 3, 4, 5]
target = 3

# nums=[4,5,6,7,0,1,2]
# target=0
s.search(nums, target)


# %%
# guofei: 改进方案
# 方案1：直接套用自己总结的binary search,while分支中将有6个判断语句，非常不利于可读性
# 方案2：分解成两个 binary search。先搜索pivot点，得到相应的rotated区域，在区域内进行binary search
# （上面的代码就是这种思路，现在用标准 binary search 方法重写）

class Solution:
    def find_pivot(self,nums):
        left,right=0,len(nums)-1
        if left==right:
            return left
        while left<right:
            mid=(left+right)//2
            if nums[mid]>=nums[0]:
                left=mid+1
            elif nums[mid]<nums[0]:
                right=mid-1
        mid=left
        if (mid+1>=len(nums)-1) or (nums[mid+1]<nums[mid]):
            return mid
        elif nums[mid]<nums[mid-1]:
            return mid-1


    def binary_search(self,nums,target,left,right):
        while left<right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
        if nums[left]==target:
            return left
        else:
            return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums)==0:
            return -1
        if nums[0]<=nums[-1]:
            return self.binary_search(nums,target,0,len(nums)-1)
        pivot=self.find_pivot(nums)
        print(pivot)
        if target>=nums[0]:
            return self.binary_search(nums,target,0,pivot)
        else:
            return  self.binary_search(nums,target,pivot+1,len(nums)-1)



nums = [3,1]
target = 0
# Solution().search()
# Solution().find_pivot(nums)
# Solution().binary_search(nums,0,0,len(nums)-1)

Solution().search(nums,target)



