# https://leetcode.com/problems/positions-of-large-groups

class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        S+='#'
        pos, i = [], 0
        len_S = len(S)
        start_point, start_letter = i, S[i]
        while i < len_S:
            if not S[i] == start_letter:
                if i - start_point >= 3:
                    pos.append([start_point, i - 1])
                start_point = i
                start_letter = S[i]
            i += 1
        return pos


S = "abcdddeeeeaabbbcd"
S='aaa'
Solution().largeGroupPositions(S)
