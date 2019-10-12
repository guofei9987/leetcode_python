# https://leetcode.com/problems/construct-the-rectangle
import numpy as np
import math
class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        L_start=math.ceil(area**0.5)
        for i in range(L_start,area+1):
            if area%i==0:
                return [i,area//i]





