# https://leetcode.com/problems/isomorphic-strings

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def onewaycheck(s,t):
            d = dict()
            for i, char1 in enumerate(s):
                if char1 in d:
                    if not d[char1] == t[i]:
                        return False
                else:
                    d[char1] = t[i]
            return True

        if not len(s) == len(t):
            return False
        if onewaycheck(s,t) and onewaycheck(t,s):
            return True
        return False

s = "ab"
t = "ca"

Solution().isIsomorphic(s, t)
