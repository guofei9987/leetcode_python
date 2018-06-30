# https://leetcode.com/problems/shortest-distance-to-a-character
class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        def one_way_len(S, C):
            len_left = []
            len_iter = 10001
            for i, j in enumerate(S):
                if C == j:
                    len_iter = 0
                len_left.append(len_iter)
                len_iter += 1
            return len_left

        len_left = one_way_len(S, C)
        len_right = one_way_len(S[::-1], C)[::-1]
        return [min(len_left[i], len_right[i]) for i in range(len(len_right))]
