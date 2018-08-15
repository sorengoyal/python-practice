#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth, val = self.getDepthAndLeftValue(root)
        return val

    def getDepthAndLeftValue(self, node):
        if node is None:
            raise Exception
        left, right = 0, 0

        if node.left is None:
            ldepth, lval = 0, node.val
        else:
            ldepth, lval = self.getDepthAndLeftValue(node.left)
        if node.right is None:
            rdepth, rval = 0, -1
        else:
            rdepth, rval = self.getDepthAndLeftValue(node.right)

        if ldepth >= rdepth:
            #print('Node:' + str(node.val) + " " + str(lval))
            return ldepth + 1, lval
        else:
            #print('Node:' + str(node.val) + " " + str(rval))
            return rdepth + 1, rval



if __name__ == '__main__':
    sln = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(sln.findBottomLeftValue(root))