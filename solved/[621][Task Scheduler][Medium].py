# https://leetcode.com/problems/task-scheduler
class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack=[]
        output=0
        for i in ops:
            if i=='C':
                output-=stack.pop()
            elif i=='D':
                point=stack[-1]*2
                stack.append(point)
                output+=point
            elif i=='+':
                point=stack[-2]+stack[-1]
                stack.append(point)
                output+=point
            else:
                point=int(i)
                stack.append(point)
                output+=point
        return output