# https://leetcode.com/problems/1-bit-and-2-bit-characters
import collections
class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        bits.pop()
        deque=collections.deque(bits)
        len_deque=len(deque)
        while len_deque>=2:
            if deque[0]:
                deque.popleft()
                deque.popleft()
                len_deque-=2
            else:
                deque.popleft()
                len_deque-=1
        if len_deque==1:
            return deque[0]==0
        else:
            return True



[1,1,0,0] # True
[1,1,1,0] # False
[1,0,0,0]