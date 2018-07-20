# https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_dict,nums2_dict=dict(),dict()
        for i in nums1:
            if i in nums1_dict:
                nums1_dict[i]+=1
            else:
                nums1_dict[i]=1

        for i in nums2:
            if i in nums1_dict:
                if i in nums2_dict:
                    if nums1_dict[i]>nums2_dict[i]:
                        nums2_dict[i]+=1
                else:
                    nums2_dict[i]=1

        output=[]
        for i in nums2_dict:
            output.extend([i]*nums2_dict[i])

        return output

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
Solution().intersect(nums1,nums2)
####################
# guofei: a better solution, some same mothod

def intersect(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    dict1 = dict()
    for i in nums1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    ret = []
    for i in nums2:
        if i in dict1 and dict1[i]>0:
            ret.append(i)
            dict1[i] -= 1
    return ret
