# https://leetcode.com/problems/backspace-string-compare

class Solution:
    def get_pure_string(self, S):
        res = []
        for i in S:
            if i == '#':
                if len(res)>0:
                    res.pop()
            else:
                res.append(i)
        return res

    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.get_pure_string(S) == self.get_pure_string(T)



S="a##c"
T="#a#c"

Solution().backspaceCompare(S,T)