# https://leetcode.com/problems/product-of-array-except-self



class Solution:
    def trap(self, height: list) -> int:
        if not height:
            return 0
        max_height=max(height)
        len_height=len(height)
        cum_max_left=[0]*len_height
        cum_max_right=[0]*len_height
        max_left,max_right=0,0
        for i in range(len_height):
            max_left=max(max_left,height[i])
            cum_max_left[i]=max_left
            j=len_height-i-1
            max_right=max(max_right,height[j])
            cum_max_right[j]=max_right
        total_area=0
        for i in range(len_height):
            total_area+=(min(cum_max_left[i],cum_max_right[i])-height[i])
        return total_area


class Solution:
    def productExceptSelf(self, nums):
        prod=1
        has_zero=0
        len_nums=len(nums)
        for idx,num in enumerate(nums):
            if num==0:
                has_zero+=1
                zero_idx=idx
                continue
            prod*=num
        if has_zero==0:
            return [int(prod/i) for i in nums]
        elif has_zero==1:
            print(zero_idx)
            output=[0]*len(nums)
            output[zero_idx]=prod
            return output
        else:
            return [0]*len(nums)

