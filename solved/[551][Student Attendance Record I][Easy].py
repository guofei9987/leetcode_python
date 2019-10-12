# https://leetcode.com/problems/student-attendance-record-i

import collections


class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return (s.count('A')<=1) and ('LLL' not in s )


"LALL" # True
'LLL' # False

'AA'.split('A')

'AA'.find('LLL')