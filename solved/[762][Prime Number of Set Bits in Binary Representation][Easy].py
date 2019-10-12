# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation





class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        prime_num_under_20 = [2, 3, 5, 7, 11, 13, 17, 19]
        out_put = 0
        for i in range(L, R + 1):
            if bin(i).count('1') in prime_num_under_20:
                out_put += 1
        return out_put


class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        return len([1 for i in range(L,R+1) if bin(i).count('1') in [2, 3, 5, 7, 11, 13, 17, 19]])


L=10
R=15
prime_num_under_20 = [2, 3, 5, 7, 11, 13, 17, 19]
out_put = 0
for i in range(L, R + 1):
    if bin(i).count('1') in prime_num_under_20:
        out_put += 1
return out_put