# https://leetcode.com/problems/find-smallest-letter-greater-than-target

class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letters_set=set(letters)
        letters_set_filter=[i for i in letters_set if target<i]
        if letters_set_filter:
            return min(letters_set_filter)
        else:
            return min(letters_set)


letters = ["c", "f", "j"]
target = "d"
Solution().nextGreatestLetter(letters,target)