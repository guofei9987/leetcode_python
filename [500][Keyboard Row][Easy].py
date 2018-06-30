# https://leetcode.com/problems/keyboard-row

class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [set('qwertyuiopQWERTYUIOP'),
        set('asdfghjklASDFGHJKL'),
        set('zxcvbnmZXCVBNM')]
        output_words = []
        for i in words:
            for row in rows:
                if set(i).issubset(row):
                    output_words.append(i)
        return output_words


# :guofei:better one from myself
words=["Hello", "Alaska", "Dad", "Peace"]

rows = [set('qwertyuiopQWERTYUIOP'),set('asdfghjklASDFGHJKL'),set('zxcvbnmZXCVBNM')]
[i for i in words for j in [0,1,2] if set(i).issubset(rows[j])]

# output_words = []
# for i in words:
#     for row in rows:
#         if set(i).issubset(row):
#             output_words.append(i)
# output_words