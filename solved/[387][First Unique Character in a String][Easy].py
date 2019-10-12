# https://leetcode.com/problems/first-unique-character-in-a-string

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d=dict()
        duplicated_set=set()
        for i,char in enumerate(s):
            if char not in duplicated_set:
                if char in d:
                    d.pop(char)
                    duplicated_set.add(char)
                else:
                    d[char]=i
        if d:
            return min(d.values())
        else:
            return -1

s = "leetcode"
s = "loveleetcode"
s= ""
s="aadadaad"
Solution().firstUniqChar(s)