# https://leetcode.com/problems/number-of-boomerangs

class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        out_put=0
        len_points=len(points)
        for i in range(len_points):
            dis_dict=dict()
            for j in range(len_points):
                if i==j:continue
                x=points[i][0]-points[j][0]
                y=points[i][1]-points[j][1]
                dis=x*x+y*y
                dis_dict[dis]=dis_dict.get(dis,0)+1
            for dis_count in dis_dict.values():
                out_put+=dis_count*(dis_count-1)
        return out_put



points = [[0, 0], [1, 0], [2, 0]]

Solution().numberOfBoomerangs(points)
