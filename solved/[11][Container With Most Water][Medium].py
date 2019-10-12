# https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: list) -> int:
        len_l=len(height)
        best=0
        for i in range(len_l-1):
            for j in range(i+1,len_l):
                area=(j-i)*min(height[i],height[j])
                if area>best:
                    best=area
        return best

# 上面这个暴力搜索，超时


class Solution:
    def maxArea(self, height: list) -> int:
        l,r=0,len(height)-1
        max_area=0
        while l<r:
            area=(r-l)*(min(height[l],height[r]))
            if area>max_area:
                max_area=area
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_area
