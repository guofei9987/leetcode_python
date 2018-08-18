# https://leetcode.com/problems/longest-palindrome

import collections
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_count=collections.Counter(s)
        odds=0
        res=0
        for i in s_count:
            res+=(s_count[i]//2)*2
            if odds==0:
                if s_count[i]%2:
                   odds=1
                   res+=1
        return res