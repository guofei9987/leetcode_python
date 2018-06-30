# encoding=utf-8
# https://leetcode.com/problems/self-dividing-numbers
class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def is_self_dividing_number(num):
            num_tmp=num
            digits_list=[]
            while num_tmp>0:
                digits_list.append(num_tmp%10)
                num_tmp=num_tmp//10
            if 0 in digits_list:
                return False
            for i in digits_list:
                if num%i!=0:
                    return False
            return True
        self_dividing_number_list=[]
        for i in range(left,right+1):
            if is_self_dividing_number(i):
                self_dividing_number_list.append(i)
        return self_dividing_number_list


#   :guofei: 一个简单的提取digits的方案

a=1234
[int(i) for i in str(a)]






