# https://leetcode.com/problems/intersection-of-two-arrays

class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1)&set(nums2))

nums1 = []
nums2 = []
Solution().intersection(nums1,nums2)
