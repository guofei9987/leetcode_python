# https://leetcode.com/problems/most-common-word
import collections
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        for i in "!?',;.":
            paragraph=paragraph.replace(i,'')
        words_count=collections.Counter(paragraph.lower().split(sep=' '))
        for i in banned:
            del words_count[i]
        return sorted(words_count.items(),key=lambda x:x[1],reverse=True)[0][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]



Solution().mostCommonWord(paragraph,banned)