# https://leetcode.com/problems/construct-string-from-binary-tree

class Solution:
    def dlr(self,root):
        return [root.val]+[self.dlr(root.left),self.dlr(root.right)] if root else [[]]
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        out_str1= str(self.dlr(t)).replace(',','').replace(' ','').replace('[','(').replace(']',')')
        while out_str1.find('())')>=0:
            out_str1=out_str1.replace('())',')')
        return out_str1[1:-1]
