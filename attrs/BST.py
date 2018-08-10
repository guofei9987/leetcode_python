# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


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

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


class Solution:
    def inOrder(self,root,list_num=[]):
        if root is None:
            return []
        list_num.append(root.val)
        if root.left:
            self.inOrder(root.left,list_num)
        if root.right:
            self.inOrder(root.right,list_num)
        return list_num

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left:
            left_values=self.inOrder(root.left,list_num=[])
            for i in left_values:
                if root.val<=i:
                    return False
        if root.right:
            right_values=self.inOrder(root.right,list_num=[])
            for i in right_values:
                if root.val>=i:
                    print(root.val,i)
                    return False
        if root.left is not None:
            if not self.isValidBST(root.left):
                return False
        if root.right is not None:
            if not self.isValidBST(root.right):
                return False
        return True


root = list2tree2([2,1,3])
# root=deserialize('[5,1,4,null,null,3,6]')
Solution().isValidBST(root)

# Solution().inOrder(root)