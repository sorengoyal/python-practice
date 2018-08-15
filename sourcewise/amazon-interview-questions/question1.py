from collections import OrderedDict
class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, s):
        n = self.root
        s = s + '\n'
        for ch in s:
            if ch not in n.children:
                n.children[ch] = Node(ch)
            n = n.children[ch]

    def getStrings(self):
        return self.getStrings_helper(self.root)

    def getStrings_helper(self, node):
        stringList = []
        print(node.val)
        children = self.getSortedKeys(node.children)
        for ch in children:
            if ch == '\n':
                stringList.append(node.val + ch)
            else:
                for s in self.getStrings_helper(node.children[ch]):
                    stringList.append(node.val + s)
            print(stringList)
        return stringList

    def getSortedKeys(self, d):
        l =  [keys for keys in d]
        l.sort()
        return l

    def __str__(self):
        pass

class Node:
    def __init__(self, val):
        self.val = val
        self.children = dict()


class Solution:
    def reorderLogs(self,logs):
        ignoredIndices = []
        t = Trie()
        for i,log in enumerate(logs):
            iden, data = self.parse(log)
            if self.containsNumbers(data):
                ignoredIndices.append(i)
                continue
            else:
                t.insert(data+'.'+iden)

        sortedList = []
        for s in t.getStrings():
            data, iden = s.split(':')
            sortedList.append(iden +' '+data)

        for i in ignoredIndices:
            sortedList.append(logs[i])

        return sortedList

if __name__ == '__main__':
    t = Trie()
    t.insert('abc.q12')
    t.insert('ab.q2')
    #print(t.root.children)
    print(t.getStrings())