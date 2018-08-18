# https://leetcode.com/problems/count-binary-substrings

class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """


s="00110011"
s="10101"

coverter={'0':'1','1':'0'}
char=s[0]
sqs,sq=[],0
for i in s:
    if i==char:
        sq+=1
    else:
        char=coverter[char]
        sqs.append(sq)
        sq=1

sqs.append(sq)
out_put=0
for i in range(len(sqs)-1):
    out_put+=min(sqs[i],sqs[i+1])
out_put
