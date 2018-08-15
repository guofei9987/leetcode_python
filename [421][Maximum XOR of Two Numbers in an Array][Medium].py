# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array

class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_XOR=0
        while nums:
            i=nums.pop()
            for j in nums:
                max_XOR=max(i^j,max_XOR)
        return max_XOR

Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])
