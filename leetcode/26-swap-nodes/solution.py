class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val) + ' ' + self.next.__str__()

def createLinkedList(l):
    if len(l) == 0:
        return None
    head = Node(l[0])
    p = head
    for n in l[1:]:
        p.next = Node(n)
        p = p.next
    return head

class Solution:
    def swapNodes(self, p):
        if p is None or p.next is None:
            return p
        head = p.next
        p.next = self.swapNodes(p.next.next)
        head.next = p
        return head

if __name__ == '__main__':
    sln = Solution()
    l = createLinkedList([1,2,3])
    print(l)
    print(sln.swapNodes(l))