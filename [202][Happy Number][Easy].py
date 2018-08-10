# https://leetcode.com/problems/happy-number

class Solution:
    def getsumsqures(self, digits):
        output = 0
        while digits > 0:
            output += (digits % 10) ** 2
            digits = digits // 10
        return output

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        stack = []
        while True:
            n = self.getsumsqures(n)
            if n == 1:
                return True
            else:
                if n in stack:
                    return False
                stack.append(n)


Solution().isHappy(19)
