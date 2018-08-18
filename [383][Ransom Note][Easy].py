# https://leetcode.com/problems/ransom-note

import collections
class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        r=collections.Counter(ransomNote)
        m=collections.Counter(magazine)
        for letter in r:
            m[letter]-=r[letter]
            if m[letter]<0:
                return False
        return True