# https://leetcode.com/problems/binary-watch
import itertools

class Solution:
    def read_hour(self, n_hour):
        return [sum(i) for i in itertools.combinations([1, 2, 4, 8], r=n_hour) if sum(i) <= 11]

    def read_min(self, n_min):
        return [sum(i) for i in itertools.combinations([1, 2, 4, 8, 16, 32], r=n_min) if sum(i) <= 59]

    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for n_hour in range(num + 1):
            n_min = num - n_hour
            if (n_hour <= 4) and (n_min <= 6):
                res.extend(['{hour}:{min:0>2}'.format(hour=hour, min=min)
                            for hour in self.read_hour(n_hour) for min in self.read_min(n_min)])
        return res


Solution().readBinaryWatch(4)

