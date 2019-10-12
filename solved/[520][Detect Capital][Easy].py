# https://leetcode.com/problems/detect-capital

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.upper()==word or word.lower()==word or word.capitalize()==word