# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii

class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>=nums[0]:
                left=mid+1
            elif nums[mid]<=nums[-1]:
                right=mid-1
        print(left)
        candidate=[left,0]
        if 0<=left-1<len(nums):
            candidate.append(left-1)
        if 0<=left+1<len(nums):
            candidate.append(left+1)
        return min([nums[i] for i in candidate])

# nums=[1,3,5]
# nums=[3,3,1]
# nums=[10,1,10,10,10]
# a=Solution().findMin(nums)


################################################


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(list(set(nums)))[0]




nums=[1,3,5]
# nums=[3,3,1]
# nums=[10,1,10,10,10]
a=Solution().findMin(nums)
a
