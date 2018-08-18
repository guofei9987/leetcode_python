# https://leetcode.com/problems/rectangle-overlap


class Solution(object):
    def isPointInTectangle(self, rec, point):
        if rec[0] < point[0] < rec[2]:
            if rec[1] < point[1] < rec[3]:
                return True
        return False

    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return self.isPointInTectangle(rec1,[rec2[0],rec2[1]]) or \
               self.isPointInTectangle(rec1,[rec2[0],rec2[3]]) or \
               self.isPointInTectangle(rec1,[rec2[2],rec2[1]]) or \
               self.isPointInTectangle(rec1,[rec2[2],rec2[3]])


rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
rec1=[7,8,13,15]
rec2=[10,8,12,20]
Solution().isRectangleOverlap(rec1,rec2)