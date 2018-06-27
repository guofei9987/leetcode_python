# https://leetcode.com/problems/valid-parentheses
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren2num_dict = {'[': 0.8, ']': -0.8, '{': 0.7, '}': -0.7, '(': 0.6, ')': -0.6}
        s_list = [paren2num_dict[i] for i in s]
        while len(s_list) >= 2:
            n1 = len(s_list)
            for i in range(n1 - 1):
                if s_list[i] + s_list[i + 1] == 0:
                    s_list.pop(i)
                    s_list.pop(i)
                    break
            n2 = len(s_list)
            if n2 == n1: return False
        if len(s_list) == 1: return False
        return True
