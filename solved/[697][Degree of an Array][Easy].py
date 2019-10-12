# https://leetcode.com/problems/degree-of-an-array
import collections


class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        nums_counter = sorted(collections.Counter(nums).items(), key=lambda x: x[1], reverse=True)
        max_frequent_num = []
        for i in nums_counter:
            if i[1] == nums_counter[0][1]:
                max_frequent_num.append(i[0])
        output = float('inf')
        for i in max_frequent_num:
            len_subarray = len_nums - nums.index(i) - nums[::-1].index(i)
            output = min(output, len_subarray)
        return output


Solution().findShortestSubArray([1,2,2,3,1,4,2])
