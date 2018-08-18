# https://leetcode.com/problems/nim-game
class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bool(n%4)