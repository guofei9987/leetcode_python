# https://leetcode.com/problems/find-the-difference

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """


import collections




class Solution(object):
    def findTheDifference(self, s, t):
        return list(collections.Counter(t)-collections.Counter(s))[0]
        # return list((collections.Counter(t) - collections.Counter(s)))[0]

s='abc'
t='aabcd'
Solution().findTheDifference(s,t)
