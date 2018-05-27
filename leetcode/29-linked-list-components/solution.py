# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next is None:
            return str(self.val)
        return str(self.val) + '->' + self.next.__str__()



class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        setG = set(G)
        p = head
        isLastRed = False
        count = 0
        while p is not None:
            if p.val in setG:
                if isLastRed is False:
                    count += 1
                    isLastRed = True
            else:
                isLastRed = False
            p = p.next
        return count

if __name__ == '__main__':
    sln = Solution()
    l = [0,1,2,3,4,5,6]
    G = [0,1,3,5]
    head = ListNode(l[0])
    p = head
    for val in l[1:]:
        p.next = ListNode(val)
        p = p.next
    print head
    print(sln.numComponents(head, G ))
