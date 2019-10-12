# https://leetcode.com/problems/next-greater-element-i

nums1 = [4,1,2]
nums2 = [1,3,4,2]

nums1 = [2,4]
nums2 = [1,2,3,4]

output_list=[]
for i in nums1:
    nums2.index(i)
    tag=-1
    for j,candidate in enumerate(nums2[nums2.index(i):]):
        if i<candidate:
            tag=candidate
            break
    output_list.append(tag)

output_list

