# https://leetcode.com/problems/add-digits

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return self.addDigits(sum(int(i) for i in str(num))) if num>=10 else num


Solution().addDigits(49)