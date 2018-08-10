# https://leetcode.com/problems/perfect-squares


class Solution(object):
    _dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            print('------------')
            print(dp)
            print([dp[-i * i] for i in range(1, int(len(dp) ** 0.5 + 1))])
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]

Solution().numSquares(5)