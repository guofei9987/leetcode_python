# https://leetcode.com/problems/median-of-two-sorted-arrays


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        len_num=len(nums1)
        if len_num%2:
            return nums1[len_num//2]*1.0
        else:
            return (nums1[len_num//2-1]+nums1[len_num//2])/2

nums1 = [1, 3]
nums2 = [2,4,5,6]
Solution().findMedianSortedArrays(nums1,nums2)