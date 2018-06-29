# https://leetcode.com/problems/hamming-distance


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x_list=[int(i) for i in bin(x)[2:]]
        bin_y_list=[int(i) for i in bin(y)[2:]]
        bin_x_list=[0]*(32-len(bin_x_list))+bin_x_list
        bin_y_list=[0]*(32-len(bin_y_list))+bin_y_list

        hamming_distance=0
        for i in range(32):
            if bin_x_list[i]!=bin_y_list[i]:
                hamming_distance+=1
        return hamming_distance


# :gufoei: 他们的更简洁的答案
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')
