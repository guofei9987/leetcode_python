# https://leetcode.com/problems/valid-anagram
import collections


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_count, t_count = collections.Counter(s), collections.Counter(t)
        return (not s_count - t_count) and (not t_count - s_count)


s = "anagram"
t = "nagaram"
s = "rat"
t = "car"
s = 'a'
t = 'ab'
Solution().isAnagram(s, t)
