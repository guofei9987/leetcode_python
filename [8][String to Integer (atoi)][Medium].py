# https://leetcode.com/problems/string-to-integer-atoi
import re


class Solution:
    regex = re.compile('-?[0-9]+')

    def myAtoi(self, str: str) -> int:
        regex = self.regex
        for a in regex.finditer(str):
            break
        return int(str[a.start():a.end()])


class Solution:
    def myAtoi(self, str: str) -> int:
        len_s=len(str)
        words=' -0123456789'
        for i,char in enumerate(str):
            if char not in words:
                i-=1
                break
        if i==-1:
            return 0
        output=int(str[:i+1])
        return output
        # return min(max(output,-2**31),2*31-1)

sol=Solution()
s="words and 987"

s="4193 with words"
# s='-'
sol.myAtoi(s)