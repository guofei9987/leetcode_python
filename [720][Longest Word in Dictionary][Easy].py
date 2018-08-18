# https://leetcode.com/problems/longest-word-in-dictionary

class Solution(object):
    def islongestword(self,word,words):
        while word:
            if not word[:-1] in words:
                return False
        return True

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        max_len=max([len(word) for word in words])
