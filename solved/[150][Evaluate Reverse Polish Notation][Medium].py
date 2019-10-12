# https://leetcode.com/problems/evaluate-reverse-polish-notation
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack=[]
        operaters={'+','-', '*', '/'}
        for s in tokens:
            print(stack)
            if s in operaters:
                b=stack.pop()
                a=stack.pop()
                if s=='+':
                    stack.append(a+b)
                elif s=='-':
                    stack.append(a-b)
                elif s=='*':
                    stack.append(a*b)
                elif s=='/':
                    stack.append(int(a/b))
            else:
                stack.append(int(s))
        return stack[0]


tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Solution().evalRPN(tokens)