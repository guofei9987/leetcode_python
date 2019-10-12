# https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort(reverse=True)
        output = 0
        for child in g:
            while s:
                cookie = s.pop()
                if child <= cookie:
                    output += 1
                    break
        return output



g=[1,2,3] # child
s= [1,1] # cookie

g=[1,2]
s= [1,2,3]
g.sort()
s.sort(reverse=True)
output=0
for child in g:
    while s:
        cookie=s.pop()
        if child<=cookie:
            output+=1
            break

output
