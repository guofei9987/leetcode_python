class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        while left < right:
            print(left)
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid - 1
        print(left)
        if nums[left] == target:
            left_index = left
        elif nums[left + 1] == target:
            left_index = left + 1
        else:
            return -1, -1

        left, right = left_index, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if nums[right] == target:
            right_index = right
        elif nums[right - 1] == target:
            right_index = right - 1
        return left_index, right_index


nums=[1,2,3,4]
target=8
a=Solution().searchRange(nums,target)
print(a)

