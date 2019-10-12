# https://leetcode.com/problems/longest-palindromic-substring

class Solution:
    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        best_len, best_p = 0, ''

        for i in range(len_s):
            length, p = self.get_longest(s, len_s, i, i)
            length -= 1
            if length > best_len:
                best_len, best_p = length, p

        for i in range(len_s - 1):
            length, p = self.get_longest(s, len_s, i, i + 1)
            if length > best_len:
                best_len, best_p = length, p
        return best_p

    def get_longest(self, s, len_s, i, j):
        length = 0
        while i >= 0 and j < len_s:
            if s[i] == s[j]:
                length += 2
                i -= 1
                j += 1
            else:
                break
        i += 1
        j -= 1
        return length, s[i:j + 1]


s = 'bbd'
sol = Solution()
# sol.get_longest(s,len(s),1,2)
sol.longestPalindrome(s)
# sol.get_longest(s)

