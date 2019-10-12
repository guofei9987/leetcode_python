# https://leetcode.com/problems/number-complement

class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        flat_dict = {'0': '1', '1': '0'}
        return int(''.join([flat_dict[i] for i in bin(num)[2:]]), base=2)



