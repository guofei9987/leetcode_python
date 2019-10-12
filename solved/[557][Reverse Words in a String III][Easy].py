# https://leetcode.com/problems/reverse-words-in-a-string-iii

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([i[::-1] for i in s.split()])




