# https://leetcode.com/problems/replace-words

class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        dict_dict = {i: len(i) for i in dict}
        dict_dict = {i: len(i) for i in dict}
        dict_values = list(set(dict_dict.values()))
        dict_values.sort()
        print(dict_values)
        words = sentence.split(sep=' ')
        for i, word in enumerate(words):
            for j in dict_values:
                if word[:j] in dict_dict:
                    words[i] = word[:j]
                    break
        return ' '.join(words)


#####################################
# %%

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:
    # https://leetcode.com/explore/learn/card/trie/147/basic-operations/1047/
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True

    def find_prefix(self, word):
        node = self.root
        prefix = ''
        for i in word:
            prefix += i
            if i not in node.children:
                return word
            else:
                if node.children[i].word:
                    return prefix
                else:
                    node = node.children[i]
        return word


class Solution:
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        tire = Trie()
        for i in dict:
            tire.insert(i)

        words=[]
        for i in sentence.split(sep=' '):
            words.append(tire.find_prefix(i))
        return ' '.join(words)



dict = ["cat", "bat", "rat"]

sentence = "the cattle was rattled by the battery"

dict = ["a", "aa", "aaa", "aaaa"]
sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"

Solution().replaceWords(dict, sentence)

tire = Trie()
for i in dict:
    tire.insert(i)

for i in sentence.split(sep=' '):
    a=tire.find_prefix(i)
    print(a)

