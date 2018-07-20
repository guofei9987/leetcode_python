class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<=1:return x
        left,right=0,x
        while left<right:
            mid=(left+right)//2
            if mid*mid<=x<(mid+1)*(mid+1):
                return mid
            elif x<mid*mid:
                right=mid
            else:
                left=mid+1


############################
#%%

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left,right=0,x
        # if left==right:
        #     return 0
        while left<right:
            mid=(left+right)//2
            if mid*mid>x:
                right=mid-1
            elif (mid+1)*(mid+1)<=x:
                left=mid+1
            elif mid*mid<=x<(mid+1)*(mid+1):
                return mid
        mid=left
        if mid*mid<=x<(mid+1)*(mid+1):
            return mid

for i in range(100):
    print(i,Solution().mySqrt(i))
# Solution().mySqrt(6)