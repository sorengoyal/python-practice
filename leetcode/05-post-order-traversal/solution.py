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
        #postorder
        if self.head is None:
            return ''
        l = self.postOrderTraversal(self.head)
        return str(l)

    def postOrderTraversal(self, node):
        if node is None:
            return []
        if node.isLeaf():
            return [node.getValue()]
        l = []
        l += self.postOrderTraversal(node.left)
        l += self.postOrderTraversal(node.right)
        l += [node.getValue()]
        return l


class Solution(object):
    def postorderTraversal(self, root):
        stack = list()
        if root is None:
            return []
        stack.append((root,''))
        if root.right is not None:
            stack.append((root,'r'))
        if root.left is not None:
            stack.append((root,'l'))

        l = []
        node, d = stack.pop()
        while len(stack) != 0:
            if d == 'l':
                if node.left is not None:
                    t = node.left
                    stack.append((t, ''))
                    if t.right is not None:
                        stack.append((t, 'r'))
                    if t.left is not None:
                        stack.append((t, 'l'))
            elif d == 'r':
                if node.right is not None:
                    t = node.right
                    stack.append((t, ''))
                    if t.right is not None:
                        stack.append((t, 'r'))
                    if t.left is not None:
                        stack.append((t, 'l'))
            elif d == '':
                l += [node.val]
            node, d = stack.pop()
        if d == '':
            l += [node.val]
        return l



if __name__== '__main__':
    sln = Solution()
    l = [3,4,5,2,1]
    tree = BinarySearchTree()
    for e in l:
        tree.insert(e)
    print(sln.postorderTraversal(tree.head))

