# https://leetcode.com/problems/single-number
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        candidate = []
        for i in nums:
            if i in candidate:
                candidate.remove(i)
            else:
                candidate.append(i)
        return candidate[0]

##########################
# guofei: see https://leetcode.com/problems/single-number/solution/
#

class Solution(object):
    def singleNumber(self, nums):
        return sum(list(set(nums)))*2 - sum(nums)

#########################
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a