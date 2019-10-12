# https://leetcode.com/problems/flipping-an-image
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[1-j for j in i[::-1]] for i in A]

solution=Solution()
# solution.flipAndInvertImage()

