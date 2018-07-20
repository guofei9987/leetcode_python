# https://leetcode.com/problems/minimum-size-subarray-sum




class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        solution=float('inf')
        tmp_sum=0
        j=0
        for i,num in enumerate(nums):
            tmp_sum+=num
            while tmp_sum>=s:
                solution=min(solution,i-j+1)
                tmp_sum-=nums[j]
                j+=1
        return 0 if solution==float('inf') else solution


s = 7
nums = [7]
Solution().minSubArrayLen(s,nums)
