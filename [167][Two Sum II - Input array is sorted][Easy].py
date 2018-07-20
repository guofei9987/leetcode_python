# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_num=len(numbers)
        numbers_set=set(numbers)
        for i in numbers_set:
            if i*2<target:
                if target-i in numbers_set:
                    return numbers.index(i)+1,numbers.index(target-i)+1
        if target%2==0:
            double_target=target//2
            double_tag=2
            double_list=[]
            for idx,num in enumerate(numbers):
                if num ==double_target:
                    double_tag-=1
                    double_list.append(idx)
                if double_tag==0:
                    return min(double_list)+1,max(double_list)+1


s=Solution()

####
# :guofei: a solution with O(n) and O(1) space
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/114371/Python3-solution-with-O(n)-and-O(1)-space/
class Solution:
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers)-1
        while True:
            psum = numbers[i] + numbers[j]
            if psum == target:
                return [i+1, j+1]
            elif psum > target:
                j -= 1
            else:
                i += 1
        return None