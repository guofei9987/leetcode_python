# https://leetcode.com/problems/binary-number-with-alternating-bits

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        bin_n=bin(n)
        odds,even=set(bin_n[2::2]),set(bin_n[3::2])
        return len(odds)+len(even)==len(odds|even)


Solution().hasAlternatingBits(10)


