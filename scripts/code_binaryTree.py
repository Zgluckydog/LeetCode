# 二叉树定义
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    # 144.二叉树的前序遍历
    def traversal1(self,root,res):
        if root == None: return
        res.append(root.val)
        self.traversal1(root.left,res)
        self.traversal1(root.right,res)

    def preorderTraversal(self,root):
        res = []
        self.traversal1(root,res)
        return res

    # 145.二叉树后序遍历
    def traversal2(self,root,res):
        if not root: return
        self.traversal2(root.left,res)
        self.traversal2(root.right,res)
        res.append(root.val)
    def postorderTraversal(self,root):
        res = []
        self.traversal2(root,res)
        return res
