# https://leetcode.com/problems/top-k-frequent-elements


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import collections
        nums_dict=collections.Counter(nums)
        soted_dict= sorted(nums_dict.items(),reverse=True,key=lambda x:x[1])[:k]
        return [x[0] for x in soted_dict]

Solution().topKFrequent(nums=[1,1,1,2,2,3],k=2)