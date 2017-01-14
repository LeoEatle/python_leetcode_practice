# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        direction = 'left'
        self.result = []
        cache1 = [root]
        cache2 = []
        self.bfs(cache1, cache2, direction)
        return self.result

    def bfs(self, cache1, cache2, direction):
        if len(cache1) is 0 and len(cache2) is 0:
            return
        else:
            layer = []
            if direction == "right":
                while len(cache1) is not 0:
                    temp = cache1.pop()
                    layer.append(temp.val)
                    if temp.right:
                        cache2.append(temp.right)
                    if temp.left:
                        cache2.append(temp.left)
                self.result.append(layer)
                cache1, cache2 = cache2, cache1
                direction = "left"
            elif direction == "left":
                while len(cache1) is not 0:
                    temp = cache1.pop()
                    layer.append(temp.val)
                    if temp.left:
                        cache2.append(temp.left)
                    if temp.right:
                        cache2.append(temp.right)
                cache1, cache2 = cache2, cache1
                direction = "right"
                self.result.append(layer)
        self.bfs(cache1, cache2, direction)





