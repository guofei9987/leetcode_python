# https://leetcode.com/problems/contains-duplicate-ii

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d=dict()
        for i,num in enumerate(nums):
            if num in d:
                if i-d[num]<=k:
                    return True
            d[num]=i
        return False


nums = [1,2,3,1]
k = 3
# nums = [1, 0, 1, 1]
# k = 1
nums =  [1,2,3,1,2,3]
k=2
Solution().containsNearbyDuplicate(nums,k)
