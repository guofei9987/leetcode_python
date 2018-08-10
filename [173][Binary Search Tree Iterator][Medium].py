# https://leetcode.com/problems/binary-search-tree-iterator

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack=[]
        while root:
            self.stack.append(root)
            root=root.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack)>0

    def next(self):
        """
        :rtype: int
        """
        node=self.stack.pop()
        x=node.right
        while x:
            self.stack.append(x)
            x=x.left
        return node.val

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def printtree(self, i=0):
        '''
        :param i:
        :return:
        打印二叉树，凹入表示法。原理是RDL遍历，旋转90度看
        '''
        tree_str=''
        if self.right:
            tree_str+=self.right.printtree(i + 1)
        if self.val:
            tree_str+=('    ' * i + '-' * 3+str(self.val)+'\n')
        if self.left:
            tree_str+=self.left.printtree(i + 1)
        return tree_str

def list2tree(i=1, list_num=[1, 2, 3]):
    if i > len(list_num):
        return None
    treenode = TreeNode(list_num[i - 1])
    treenode.left = list2tree(2 * i, list_num)
    treenode.right = list2tree(2 * i + 1, list_num)
    return treenode



def list2tree2(nums):
  # 与我写的 list2tree 的区别是：对空值不再生成子节点，之后的数据也不会作为这个空节点的子节点，而是跳过，因此更加节省空间。
    if not nums:
        return None
    nodes = [None if val is None else TreeNode(val)
             for val in nums]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# root=list2tree(list_num=[41,37,44,24,39,42,48,1,35,38,40,None,43,46,49,0,2,30,36,None,None,None,None,None,None,45,47,None,None,None,None,None,4,29,32,None,None,None,None,None,None,3,9,26,None,31,34,None,None,7,11,25,27,None,None,33,None,6,8,10,16,None,None,None,28,None,None,5,None,None,None,None,None,15,19,None,None,None,None,12,None,18,20,None,13,17,None,None,22,None,14,None,None,21,23])
root=list2tree2([41,37,44,24,39,42,48,1,35,38,40,None,43,46,49,0,2,30,36,None,None,None,None,None,None,45,47,None,None,None,None,None,4,29,32,None,None,None,None,None,None,3,9,26,None,31,34,None,None,7,11,25,27,None,None,33,None,6,8,10,16,None,None,None,28,None,None,5,None,None,None,None,None,15,19,None,None,None,None,12,None,18,20,None,13,17,None,None,22,None,14,None,None,21,23])

i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())
v


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())