# https://leetcode.com/problems/add-and-search-word-data-structure-design

class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word = False
        self.children = dict()


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = TrieNode()
            node = node.children[i]
        node.word = True

    def ismatch(self, node, word):
        for i,char in enumerate(word):
            if not word:return node.word
            if char in node.children:
                node = node.children[char]
            elif char == '.':
                for j in node.children:
                    if self.ismatch(node.children[j],word[i+1:]):
                        return True
            else:
                return False
        return node.word

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.ismatch(self.root,word)


s=WordDictionary()
# s.addWord("bad")
# s.addWord("dad")
# s.addWord("mad")
# s.search("pad")
# s.search("bad")
# s.search(".ad")# -> true
# s.search("b..")# -> true

s.addWord('a')
s.addWord('a')
s.search('.')
s.search('.a')
s.search('aa')
# s.search('')
# s.search('.a')
# s.search('a.')