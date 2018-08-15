# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        import collections
        A, B = collections.Counter(A.split(sep=' ')), collections.Counter(B.split(sep=' '))
        A_unique, B_unique = {i for i in A if A[i] == 1}, {i for i in B if B[i] == 1}
        return list((A_unique - B.keys()) | (B_unique - A.keys()))


A = "apple apple"
B = "banana"

A="s z z z s"
B="s z ejt"
Solution().uncommonFromSentences(A, B)
