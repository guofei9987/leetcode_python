# https://leetcode.com/problems/excel-sheet-column-number
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        for i in s: num = num * 26 + (ord(i) - 64)
        return num
