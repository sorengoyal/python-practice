class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = None
        for n in nums:
            root = self.insert(root, n)
            #self.printTree(root)
            #print()
        return root

    def insert(self, root, n):
        if root is None:
            return TreeNode(n)
        if n > root.val:
            node = TreeNode(n)
            node.left = root
            return node
        else:
            root.right = self.insert(root.right, n)
            return root

    def printTree(self, node):
        if node is None:
            return
        print(node.val, end=' ')
        print('(', end='')
        self.printTree(node.left)
        print(',', end ='')
        self.printTree(node.right)
        print(')', end=' ')

if __name__ == '__main__':
    sln = Solution()
    sln.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])