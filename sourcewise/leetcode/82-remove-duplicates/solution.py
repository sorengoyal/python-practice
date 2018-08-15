# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def createList(l):
    head = ListNode(l[0])
    p = head
    for val in l[1:]:
        p.next = ListNode(val)
        p = p.next
    return head
def dumpList(head):
    p = head
    s = ''
    while p is not None:
        s += str(p.val)
        p = p.next
    return s

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        begin = ListNode(None)
        begin.next = head
        p = begin
        q = head
        val = q.val
        q = q.next
        while q is not None:
            if q.val == val:
                p.next = q
                q = q.next

            else:
                if p.next.val != val:
                    p.next = p.next.next
                    p = p.next
                val = q.val
                q = q.next
        return begin.next


if __name__ == '__main__':
    head = createList([1,2,2,3,3,4,5])
    sln = Solution()
    print(dumpList(sln.deleteDuplicates(head)))