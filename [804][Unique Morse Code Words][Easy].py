# https://leetcode.com/problems/unique-morse-code-words

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letter_list = list('abcdefghijklmnopqrstuvwxyz')
        morse_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                      "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        morse2letter = dict(zip(letter_list, morse_list))
        morse_list = set() # guofei: 这里用set比用list快相当多
        for word in words:
            morse_tmp = ''
            for i in word:
                morse_tmp += morse2letter[i]
            morse_list.add(morse_tmp)
        return len(set(morse_list))


solution=Solution()
solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
