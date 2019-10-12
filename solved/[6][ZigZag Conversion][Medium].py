# https://leetcode.com/problems/zigzag-conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or (len(s)<numRows):
            return s
        output = [''] * numRows
        idx = 0
        step = 1
        for x in s:
            output[idx] += x
            idx += step
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
        return ''.join(output)



s = "PAYPALISHIRING"
numRows = 3

sol=Solution()
sol.convert(s,3)