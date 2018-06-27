# https://leetcode.com/problems/roman-to-integer
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman2num_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        s_list=[roman2num_dict[i] for i in s[::-1]]
        y=0
        print(s_list)
        while len(s_list)>=2:
            if s_list[0]>s_list[1]:
                y+=s_list.pop(0)-s_list.pop(0)
            else:y+=s_list.pop(0)
        if len(s_list)==1:
            y+=s_list[0]
        return y