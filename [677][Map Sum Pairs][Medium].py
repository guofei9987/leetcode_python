# https://leetcode.com/problems/map-sum-pairs
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.word = False
        self.count = 0
        self.children = dict()


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        count_key=self.search(key)
        print(count_key)
        node = self.root
        for i in key:
            if i not in node.children:
                node.children[i] = TrieNode()
                node.children[i].count = val
            else:
                node.children[i].count += (val-count_key)
            node = node.children[i]
        node.word = True

    def search(self, word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        if node.word:
            return node.count
        else:
            return 0

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        for i in prefix:
            if i not in node.children:
                return 0
            node = node.children[i]
        return node.count


# obj = MapSum()
# obj.insert('aa', 3)
# obj.sum('a')
# obj.insert('aa', 2)
# print('----------')
# obj.sum('a')


obj=MapSum()
obj.insert('apple',3)
obj.sum('ap')
obj.insert('app',2)
obj.sum('ap')

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
