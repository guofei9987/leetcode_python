# https://leetcode.com/problems/letter-case-permutation

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if S:
            if S[0] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                return [char+j for char in [S[0].lower(),S[0].upper()] for j in self.letterCasePermutation(S[1:])]
            else:
                return [S[0]+j for j in self.letterCasePermutation(S[1:])]
        else:
            return ['']


S="a1b2"
Solution().letterCasePermutation(S)
#
# Solution().letterCasePermutation('2')