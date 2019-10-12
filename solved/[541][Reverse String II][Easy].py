# https://leetcode.com/problems/reverse-string-ii

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        len_s = len(s)
        print(len_s)
        for i in range(len_s // (2 * k) + 1):
            res += (s[i * 2 * k:i * 2 * k + k][::-1] + s[i * 2 * k + k:i * 2 * k + 2 * k])
        return res


s = "abcdefg"
k = 2

Solution().reverseStr(s, k)
