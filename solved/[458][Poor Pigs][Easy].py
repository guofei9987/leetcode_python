# https://leetcode.com/problems/poor-pigs
import math
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        max_try=math.ceil(minutesToTest/float(minutesToDie))
        return int(math.ceil(math.log2(buckets)/math.log2(max_try+1)))

