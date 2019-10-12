# https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d=dict()
        for word in strs:
            str_sorted=''.join(sorted(word))
            if str_sorted in d:
                d[str_sorted].append(word)
            else:
                d[str_sorted]=[word]
        return list(d.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Solution().groupAnagrams(strs)

