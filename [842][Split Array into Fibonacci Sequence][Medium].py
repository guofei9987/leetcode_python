# https://leetcode.com/problems/split-array-into-fibonacci-sequence

S="I speak Goat Latin"

vowel='aeiouAEIOU'
words=S.split(sep=' ')
for i,word in enumerate(words):
    if word[0] in vowel:
        words[i]=word+'ma'+'a'*(i+1)
    else:
        words[i]=word[1:]+word[0]+'ma'+'a'*(i+1)
print(' '.join(words))


class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vowel = 'aeiouAEIOU'
        words = S.split(sep=' ')
        for i, word in enumerate(words):
            if word[0] in vowel:
                words[i] = word + 'ma' + 'a' * (i + 1)
            else:
                words[i] = word[1:] + word[0] + 'ma' + 'a' * (i + 1)
        return ' '.join(words)
