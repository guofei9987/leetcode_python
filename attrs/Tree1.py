# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def InOrder(self, root):  # LDR
        return [] if (root is None) else self.InOrder(root.left) + [root.val] + self.InOrder(root.right)

    def PreOrder(self, root):  # DLR
        return [] if (root is None) else [root.val] + self.PreOrder(root.left) + self.PreOrder(root.right)

    def PostOrder(self, root):  # LRD
        return [] if (root is None) else self.PostOrder(root.left) + self.PostOrder(root.right) + [root.val]

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

    def find_track(self, num, root, track_str=''):
        '''
        二叉树搜索
        :param num:
        :param root:
        :param track_str:
        :return:
        '''
        track_str = track_str + str(root.val)
        if root.val == num:
            return track_str
            # print(track_str)
        if root.left is not None:
            self.find_track(num, root.left, track_str + ' ->left-> ')
        if root.right is not None:
            self.find_track(num, root.right, track_str + ' ->right-> ')

    def list2tree(self, i=1, list_num=[]):
        # 顺序结构转链式结构
        # 节点标号从1开始
        if i > len(list_num):
            return None
        treenode = TreeNode(list_num[i - 1])
        treenode.left = self.list2tree(2 * i, list_num)
        treenode.right = self.list2tree(2 * i + 1, list_num)
        return treenode

    # 还未完成
    def tree2list(self):
        pass

    def list2tree2(self, nums):
        # 与 list2tree 的区别是：对空值不再生成子节点，之后的数据也不会作为这个空节点的子节点，而是跳过，因此更加节省空间。
        if not nums:
            return None
        nodes = [None if val is None else TreeNode(val) for val in nums]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

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

    def drawtree(self, root):
        # 用 turtle 画 Tree，比纯字符串美观，但慢
        def height(root):
            return 1 + max(height(root.left), height(root.right)) if root else -1

        def jumpto(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()

        def draw(node, x, y, dx):
            if node:
                t.goto(x, y)
                jumpto(x, y - 20)
                t.write(node.val, align='center', font=('Arial', 12, 'normal'))
                draw(node.left, x - dx, y - 60, dx / 2)
                jumpto(x, y - 20)
                draw(node.right, x + dx, y - 60, dx / 2)

        import turtle
        t = turtle.Turtle()
        t.speed(0);
        turtle.delay(0)
        h = height(root)
        jumpto(0, 30 * h)
        draw(root, 0, 30 * h, 40 * h)
        t.hideturtle()
        turtle.mainloop()

    # 只针对BST的
    def isValidBST(self, root):
        # 判断是否是BST
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))

    def searchBST(self, root, val):
        # 搜索 BST
        if root and val < root.val:
            return self.searchBST(root.left, val)
        elif root and val > root.val:
            return self.searchBST(root.right, val)
        return root

    def insertIntoBST(self, root, val):
        """
        把值 val 插入到BST中
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        elif root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        return root

    def deleteNode(self, root, key):
        """
        删除节点的方式有很多种：左子节点提升，右子节点提升，下面这个也是一种思路
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            else:
                tmp, mini = root.right, root.right.val
                while tmp.left:
                    tmp, mini = tmp.left, tmp.left.val
                root.val = mini
                root.right = self.deleteNode(root.right, root.val)
        return root


list_num = [5, 3, 6, 2, 4, None, 7]
key = 3
root = Solution().list2tree2(list_num)

print(Solution().PrintTree(root))
a = Solution().deleteNode(root, key)
print(Solution().PrintTree(a))
# drawtree(list2tree2([2, 1, 3, 0, 7, 9, 1, 2, None, 1, 0, None, None, 8, 8, None, None, None, None, 7]))
