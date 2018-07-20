# https://leetcode.com/problems/find-k-closest-elements

class Solution:
    def binary_search(self,nums,target):
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                return mid
        return left
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        left,right=0,len(arr)-1-k
        while left<right:
            mid=






arr=[1,2,3,4,5]
k=4
x=3
Solution().findClosestElements(arr,k,x)