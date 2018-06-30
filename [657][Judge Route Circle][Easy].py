# https://leetcode.com/problems/judge-route-circle

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        moves2num={'R':1,'L':-1,'U':1j,'D':-1j}
        moves_num=[moves2num[i] for i in moves]
        moves_end=sum(moves_num)
        return moves_end==0

# : guofei: a better answer
#####################################
class Solution:
    def judgeCircle(self, moves):
        l, r, u, d = map(moves.count, 'LRUD')
        return l == r and u == d