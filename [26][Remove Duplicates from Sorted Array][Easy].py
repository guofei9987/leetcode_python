# https://leetcode.com/problems/remove-duplicates-from-sorted-array


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums=len(nums)
        if len_nums==0:return
        last_num=nums[0]
        i=1
        while i<len_nums:
            if nums[i]==last_num:
                nums.pop(i)
                len_nums-=1
            else:
                last_num = nums[i]
                i+=1




nums=[]
Solution().removeDuplicates(nums)
print(nums)