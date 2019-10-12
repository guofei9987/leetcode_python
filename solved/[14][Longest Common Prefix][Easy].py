# https://leetcode.com/problems/longest-common-prefix

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def CommanPrefix(n,strs):
            is_comman=True
            for i in strs:
                if not i[:n]==strs[0][:n]:
                    return False
            return is_comman
        if len(strs)==0:return ''
        n=0
        while CommanPrefix(n,strs):
            n+=1
            if n>len(strs[0]):break
        return strs[0][:n-1]