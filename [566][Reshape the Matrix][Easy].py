# https://leetcode.com/problems/reshape-the-matrix
import numpy as np


class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not len(nums) * len(nums[0]) == r * c:
            return nums
        count_raw = len(nums)
        count_col = len(nums[0])
        all_elements = [nums[j][i] for j in range(count_raw) for i in range(count_col)]
        output = []
        for i in range(r):
            output.append(all_elements[i * c:(i + 1) * c])
        return output



###############################
# guofei: I find numpy is available in leetcode!
# but is much slower
import numpy as np
class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not len(nums) * len(nums[0]) == r * c:
            return nums
        return np.array(nums).reshape(r,c).tolist()