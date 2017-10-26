class Node:
    def __init__(self, value):
        self.value = None
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

    def hasLeft(self):
        return not (self.left is None)

    def hasRight(self):
        return not (self.right is None)

    def isLeaf(self):
        return self.left is None and self.right is None

    def __str__(self):
        return self.value

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
        if value <= node.value:
            if node.hasLeft():
                self.insert_helper(node.left(), value)
            else:
                node.addLeft(value)
        else:
            if node.hasRight():
                self.insert_helper(node.right(), value)
            else:
                node.addRight(value)



    def __str__(self):
        #postorder
        if self.head is None:
            return ''

        def postOrderTraversal(self, node):
            if node.isLeaf():
                return [str(node)]
            l = []
            l += postOrderTraversal(node.left)
            l += postOrderTraversal(node.right)
            l += [node.value]
            return l


class Solution(object):
    def postorderTraversal(self, root):
        print(root)


if __name__== '__main__':
    sln = Solution()
    l = [1,2,3]
    tree =BinarySearchTree()
    for e in l:
        tree.insert(e)
    print(tree)

