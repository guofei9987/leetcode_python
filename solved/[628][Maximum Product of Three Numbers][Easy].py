# https://leetcode.com/problems/maximum-product-of-three-numbers
import itertools
class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        positive_nums=[i for i in nums if i>=0]
        negative_nums=[i for i in nums if i<0]
        positive_nums.sort()
        negative_nums.sort()
        nums_candidate=positive_nums[-3:]+negative_nums[:3]
        res=nums_candidate[0]*nums_candidate[1]*nums_candidate[2]
        for i in itertools.combinations(nums_candidate,r=3):
            res=max(res,i[0]*i[1]*i[2])
        return res

nums=[1,2,3,4,-5,-6,-1]
nums=[1,-2,-3]
Solution().maximumProduct(nums)