# https://leetcode.com/problems/reverse-words-in-a-string

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])



s="the sky is blue"
Solution().reverseWords(s)