# https://leetcode.com/problems/rotate-string

class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if A==B:return True
        for i in range(len(A)):
            if A[i :] + A[:i] == B:
                return True
        return False


A = 'abcde'
B = 'cdeab'

Solution().rotateString(A, B)
