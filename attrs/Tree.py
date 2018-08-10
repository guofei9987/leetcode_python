# Definition for a binary tree node.
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
        tree_str = ''
        if self.right:
            tree_str += self.right.printtree(i + 1)
        if self.val:
            tree_str += ('    ' * i + '-' * 3 + str(self.val) + '\n')
        if self.left:
            tree_str += self.left.printtree(i + 1)
        return tree_str

    def PreOrder(self, list_num=[]):  # DLR
        list_num.append(self.val)
        if self.left is not None:
            self.left.PreOrder(list_num=list_num)
        if self.right is not None:
            self.right.PreOrder(list_num=list_num)
        return list_num

    def InOrder(self, list_num=[]):  # LDR
        if self.left is not None:
            self.left.InOrder(list_num=list_num)
        list_num.append(self.val)
        if self.right is not None:
            self.right.InOrder(list_num=list_num)
        return list_num

    def PostOrder(self, list_num=[]):  # LRD
        if self.left is not None:
            self.left.PostOrder(list_num=list_num)
        if self.right is not None:
            self.right.PostOrder(list_num=list_num)
        list_num.append(self.val)
        return list_num

    def find_track(self, num, track_str=''):
        track_str = track_str + str(self.val)
        if self.val == num:
            print(track_str)
        if self.left is not None:
            self.left.find_track(num, track_str + ' ->left-> ')
        if self.right is not None:
            self.right.find_track(num, track_str + ' ->right-> ')


# 顺序结构转链式结构
# 第i个节点（编号从1开始）
def list2tree(i=1, list_num=[1, 2, 3]):
    if i > len(list_num):
        return None
    treenode = TreeNode(list_num[i - 1])
    treenode.left = list2tree(2 * i, list_num)
    treenode.right = list2tree(2 * i + 1, list_num)
    return treenode


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorder(self, root):  # LDR
        return [] if (root is None) else self.inorder(root.left) + [root.val] + self.inorder(root.right)

    def preorder(self, root):  # DLR
        return [] if (root is None) else [root.val] + self.preorder(root.left) + self.preorder(root.right)

    def postorder(self, root):  # LRD
        return [] if (root is None) else self.inorder(root.left) + self.inorder(root.right) + [root.val]

    # 未完待续
    def printtree(self, root,i=0):
        '''
        打印二叉树，凹入表示法。原理是RDL遍历，旋转90度看
        '''
        tree_str = ''
        if root.right:
            tree_str += self.printtree(root.right,i + 1)
        if root.val:
            tree_str += ('    ' * i + '-' * 3 + str(self.val) + '\n')
        if root.left:
            tree_str += self.printtree(root.left,i + 1)
        return tree_str

    # 未完待续
    def find_track(self, num, track_str=''):
        track_str = track_str + str(self.val)
        if self.val == num:
            print(track_str)
        if self.left is not None:
            self.left.find_track(num, track_str + ' ->left-> ')
        if self.right is not None:
            self.right.find_track(num, track_str + ' ->right-> ')

    # 需要改造
    def list2tree(self,i=1, list_num=[1, 2, 3]):
        # 顺序结构转链式结构
        # 节点标号从1开始
        if i > len(list_num):
            return None
        treenode = TreeNode(list_num[i - 1])
        treenode.left = self.list2tree(2 * i, list_num)
        treenode.right = self.list2tree(2 * i + 1, list_num)
        return treenode

    # 需要改造
    def tree2list():
        pass

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

    # LeetCode官方版本
    # deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]')
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

    def drawtree(root):
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
        inorder = self.inorder(root)
        return inorder == list(sorted(set(inorder)))


#
# def tree2list():
#     pass
#
#
list_num = [1, 2, 3, 4, 5, 6, 7]
tree = Solution().list2tree(list_num=list_num)


c = tree.printtree()
print(c)
d = tree.InOrder()
print(d)

# drawtree(list2tree2([2, 1, 3, 0, 7, 9, 1, 2, None, 1, 0, None, None, 8, 8, None, None, None, None, 7]))


# def deserialize(string):
#     if string == '{}':
#         return None
#     nodes = [None if val == 'null' else TreeNode(int(val))
#              for val in string.strip('[]{}').split(',')]
#     print(nodes)
#     kids = nodes[::-1]
#     root = kids.pop()
#     for node in nodes:
#         if node:
#             if kids: node.left = kids.pop()
#             if kids: node.right = kids.pop()
#     return root
#
#
# def list2tree2(nums):
#     if not nums:
#         return None
#     nodes = [None if val is None else TreeNode(val)
#              for val in nums]
#     kids = nodes[::-1]
#     root = kids.pop()
#     for node in nodes:
#         if node:
#             if kids: node.left = kids.pop()
#             if kids: node.right = kids.pop()
#     return root
#
#
# def drawtree(root):
#     def height(root):
#         return 1 + max(height(root.left), height(root.right)) if root else -1
#
#     def jumpto(x, y):
#         t.penup()
#         t.goto(x, y)
#         t.pendown()
#
#     def draw(node, x, y, dx):
#         if node:
#             t.goto(x, y)
#             jumpto(x, y - 20)
#             t.write(node.val, align='center', font=('Arial', 12, 'normal'))
#             draw(node.left, x - dx, y - 60, dx / 2)
#             jumpto(x, y - 20)
#             draw(node.right, x + dx, y - 60, dx / 2)
#
#     import turtle
#     t = turtle.Turtle()
#     t.speed(0);
#     turtle.delay(0)
#     h = height(root)
#     jumpto(0, 30 * h)
#     draw(root, 0, 30 * h, 40 * h)
#     t.hideturtle()
#     turtle.mainloop()
#

# drawtree(deserialize('[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))
# a=list2tree2([2, 1, 3, 0, 7, 9, 1, 2, None, 1, 0, None, None, 8, 8, None, None, None, None, 7])
# drawtree(a)
# drawtree(list2tree2([2, 1, 3, 0, 7, 9, 1, 2, None, 1, 0, None, None, 8, 8, None, None, None, None, 7]))
