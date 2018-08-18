# https://leetcode.com/problems/base-7


class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num > 0:
            sign = ''
        elif num<0:
            sign = '-'
            num = -num
        elif num==0:
            sign='0'
        res_list = []
        while num:
            res_list.append(str(num % 7))
            num = num // 7
        return sign+''.join(res_list[::-1])


num = -7

Solution().convertToBase7(num)
