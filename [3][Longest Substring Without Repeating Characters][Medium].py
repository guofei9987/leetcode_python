# https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        def issubstring(substring):
            return len(substring)==len(set(substring))
        len_str=len(s)
        output=len(set(s))
        while True:
            for i in range(len_str-output+1):
                if issubstring(s[i:i+output]):
                    return output
            output-=1






s="abcabcbb"
s="bbbbb"
s="pwwkew"
Solution().lengthOfLongestSubstring(s)


