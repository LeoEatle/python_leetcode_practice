# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #注意python中的静态方法(@staticmethod),类方法(@classmethod必须有cls参数),普通方法(必须有self参数)的区别
    #这里只是一个普通的函数(在类的内部)
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = [0]

        def findSum(root, isLeft):
            if not root:
                return
            if isLeft and not root.left and not root.right:
                sum[0] = sum[0] + root.val
                return
            findSum(root.left, True)
            findSum(root.right, False)

        findSum(root, False)
        return sum[0]