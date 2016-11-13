#coding: utf-8
import TreeNode
class Solution(object):
    def getSum(self, node, curSum):

        if node is None:
            return
        curSum = curSum + node.val
        if self.targetSum == curSum and not node.left and not node.right:#To ensure that this path if from root to leaf
            self.ifExist = True
            return
        self.getSum(node.left, curSum)
        self.getSum(node.right, curSum)

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:
            return False
        self.targetSum = sum
        self.ifExist = False
        curSum = 0
        self.getSum(root, curSum)
        print self.ifExist

treenode = TreeNode.TreeNode(3)
s = Solution()
s.hasPathSum(treenode,  3)
