# https://leetcode.com/problems/number-of-lines-to-write-string

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        widths_total=[widths[ord(i)-97] for i in S]
        margin_left=100
        line=1
        for i in widths_total:
            if margin_left<i:
                line+=1
                margin_left=100
            margin_left-=i
        return [line,100-margin_left]


widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
S = "bbbcccdddaaabbbbbbbbbbbbbbbbbbbbbbb"


# :guofei: a better on from lee215
def numberOfcurs( widths, S):
    res, cur = 1, 0
    for i in S:
        width = widths[ord(i) - ord('a')]
        res += 1 if cur + width > 100 else 0 # ！notice this
        cur = width if cur + width > 100 else cur + width
    return [res, cur]

numberOfcurs(widths,S)