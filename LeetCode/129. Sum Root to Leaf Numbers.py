# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        self.answer = 0
        self.dfs(root, 0)
        return self.answer

    def dfs(self, root, cache):
        cache = cache*10 + root.val
        if root.left == None and root.right == None:
            self.answer = cache + self.answer
        if root.left != None:
            # cache = cache + root.left.val
            self.dfs(root.left, cache)
        if root.right != None:
            # cache = cache + root.right.val
            self.dfs(root.right, cache)