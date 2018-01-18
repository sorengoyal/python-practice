class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.parent = None

    def setRight(self, node):
        self.right = node
        node.parent = self

    def setLeft(self, node):
        self.left = node
        node.parent = self

    def addLeft(self, value):
        node = Node(value)
        self.left = node
        node.parent = self

    def addRight(self, value):
        node = Node(value)
        self.right = node
        node.parent = self

    def getValue(self):
        return self.val

    def getRight(self):
        return self.right

    def getLeft(self):
        return self.left

    def getParent(self):
        return self.parent

    def hasLeft(self):
        return not (self.left is None)

    def hasRight(self):
        return not (self.right is None)

    def isLeaf(self):
        return self.left is None and self.right is None

    def __str__(self):
        print(self.val)
        return str(self.val)

class BinarySearchTree:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head is None:
            node = Node(value)
            self.head = node
            return

        self.insert_helper(self.head, value)

    def insert_helper(self, node, value):
        if value <= node.getValue():
            if node.hasLeft():
                self.insert_helper(node.getLeft(), value)
            else:
                node.addLeft(value)
        else:
            if node.hasRight():
                self.insert_helper(node.getRight(), value)
            else:
                node.addRight(value)

    def __str__(self):
        return self.printTree(self.head)

    def printTree(self, node):
        if node is None:
            return ''
        return str(node.val) + ' (' + self.printTree(node.left) + ',' + self.printTree(node.right) + ')'

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, node):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if node is None:
            return []
        left = self.largestValues(node.left)
        right = self.largestValues(node.right)
        if len(left) == 0:
            return [node.val] + right
        elif len(right) == 0:
            return [node.val] + left
        else:
            return [node.val] + [ a if a >= b else b for a,b in zip(left, right)]

if __name__== '__main__':
    sln = Solution()
    l = [10,5,15,6,20]
    tree = BinarySearchTree()
    for e in l:
        tree.insert(e)
    print(tree)
    print(sln.largestValues(tree.head))
