# https://leetcode.com/problems/longest-continuous-increasing-subsequence

class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 0
        i,len_nums,len_sub,max_len_sub=0,len(nums),1,1
        while i<len_nums-1:
            if nums[i]<nums[i+1]:
                len_sub+=1
            else:
                max_len_sub,len_sub=max(len_sub,max_len_sub),1
            i+=1
        return max(max_len_sub,len_sub)
