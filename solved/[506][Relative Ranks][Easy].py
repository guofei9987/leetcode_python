# https://leetcode.com/problems/relative-ranks

class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums_sorted=sorted(nums,reverse=True)
        rank=[nums_sorted.index(i)+1 for i in nums]
        print(rank)
        if 1 in rank:
            rank[rank.index(1)]="Gold Medal"
        if 2 in rank:
            rank[rank.index(2)] = "Silver Medal"
        if 3 in rank:
            rank[rank.index(3)] = "Bronze Medal"
        for i in range(len(rank)):
            rank[i]=str(rank[i])
        return rank

nums=[5, 4, 3, 2, 1]
Solution().findRelativeRanks(nums)