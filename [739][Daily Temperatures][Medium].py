# https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        output_list=[0]*len(temperatures)
        stack=[]
        pointer=0
        for i in temperatures:
            while True:
                if len(stack)>0:
                    if i>stack[-1][1]:
                        output_list[stack[-1][0]]=pointer-stack[-1][0]
                        stack.pop()
                    else:
                        break
                else:
                    break
            stack.append((pointer,i))
            pointer+=1
        return output_list




temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Solution().dailyTemperatures(temperatures)