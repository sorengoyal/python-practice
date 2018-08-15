class Node:
    def __init__(self, val):
        self.val = val
        self.children = dict()


class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, text):
        n = self.root
        for ch in text:
            if ch not in n.children:
                n.children[ch] = Node(ch)
            n = n.children[ch]
        if '\n' not in n.children:
            n.children['\n'] = 1
        else:
            n.children['\n'] += 1

    def getAllTextInOrder(self):
        return self.getAllTextInOrder_helper(self.root)

    def getAllTextInOrder_helper(self, node):
        textList = []
        children = self.getSortedKeys(node.children)
        for ch in children:
            if ch == '\n':
                for i in range(node.children['\n']):
                    textList.append(node.val)
            else:
                for text in self.getAllTextInOrder_helper(node.children[ch]):
                    textList.append(node.val + text)
        return textList

    def getSortedKeys(self, d):
        return sorted([key for key in d])


def reorderElements(logFileSize, logLines):
    ignoredIndices = []
    trie = Trie()
    for i, line in enumerate(logLines):
        iden, data = parseLogLine(line)
        if containsNumber(data):
            ignoredIndices.append(i)
        else:
            trie.insert(data + '.' + iden)

    sortedList = []
    for text in trie.getAllTextInOrder():
        data, iden = text.split('.')
        sortedList.append(iden + ' ' + data)
    for i in ignoredIndices:
        sortedList.append(logLines[i])
    if len(sortedList) != logFileSize:
        raise Exception(str(logLines) + str(sortedList))
    return sortedList


def parseLogLine(line):
    i = line.index(' ')
    return line[:i], line[i:]


def containsNumber(data):
    for d in data.split(' '):
        if d.isdigit():
            return True
    return False

logLines = ['ab8 123']
print(reorderElements(1, logLines))