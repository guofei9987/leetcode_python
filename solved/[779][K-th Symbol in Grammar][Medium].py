# https://leetcode.com/problems/k-th-symbol-in-grammar

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        return self.kthGrammar1(N, K - 1)

    def kthGrammar1(self, N: int, K: int) -> int:
        if K == 0:
            return 0
        a = self.kthGrammar1(N - 1, K // 2)
        b = K % 2
        return a ^ b