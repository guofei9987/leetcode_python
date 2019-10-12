# https://leetcode.com/problems/lemonade-change/description/

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        chages={5:0,10:0}
        for i in bills:
            if i==5:
                chages[5]+=1
            if i==10:
                chages[10]+=1
                chages[5]-=1
            if i==20:
                if chages[10]>=1:
                    chages[10]-=1
                    chages[5]-=1
                else:
                    chages[5]-=3
            if chages[5]<0:
                return False
        return True