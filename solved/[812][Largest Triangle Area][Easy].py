# https://leetcode.com/problems/largest-triangle-area
import numpy as np


class Solution:
    def cal_aera(self, points3):
        a = np.array(points3)
        # a.

    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """


def cal_area(points3):
    a = np.concatenate([points3])
    b = np.linalg.det(a)
    print(b)


points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]

areas = []
len_points = len(points)
for i in range(len_points):
    for j in range(i + 1, len_points):
        for k in range(j + 1, len_points):
            areas.append(np.linalg.det(np.array([points[c] + [1] for c in [i, j, k]])))

# %%

class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        import numpy as np
        len_points = len(points)
        areas_list = [np.linalg.det(np.array([points[c] + [1] for c in [i, j, k]]))
                 for i in range(len_points)
                 for j in range(i + 1, len_points)
                 for k in range(j + 1, len_points)]
        return float(max(0.5 * np.abs(i) for i in areas_list))

points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
a=Solution().largestTriangleArea(points)

