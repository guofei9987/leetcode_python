# https://leetcode.com/problems/majority-element
import collections
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter=collections.Counter(nums)
        return sorted(counter.items(),key=lambda x:x[1],reverse=True)[0][0]


Solution().majorityElement([2,2,1,1,1,2,2])