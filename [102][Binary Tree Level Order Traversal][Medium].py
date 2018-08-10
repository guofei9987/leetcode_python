# https://leetcode.com/problems/binary-tree-level-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1:
    def PrintTree(self, root, i=0):
        '''
        打印二叉树，凹入表示法。原理是RDL遍历，旋转90度看
        '''
        tree_str = ''
        if root.right:
            tree_str += self.PrintTree(root.right, i + 1)
        if root.val:
            tree_str += ('    ' * i + '-' * 3 + str(root.val) + '\n')
        if root.left:
            tree_str += self.PrintTree(root.left, i + 1)
        return tree_str

    def deserialize(self, string):
        # LeetCode官方版本
        # deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')
        if string == '{}':
            return None
        nodes = [None if val == 'null' else TreeNode(int(val)) for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        import collections
        level = 0
        deque = collections.deque([(root,level)])
        output=[]
        while deque:
            tmp_root,level = deque.popleft()
            if tmp_root.left: deque.append((tmp_root.left,level+1))
            if tmp_root.right: deque.append((tmp_root.right,level+1))
            if len(output)<=level:
                output.append([tmp_root.val])
            else:
                output[level].append(tmp_root.val)
        return output


a=Solution1().deserialize('[3,9,20,null,null,15,7]')
Solution().levelOrder(a)