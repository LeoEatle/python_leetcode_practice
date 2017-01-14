# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == None or len(lists) == 0:
            return None
        while len(lists) > 1:
            #l = lists.pop()

            lists.append(self.merge(lists.pop(), lists.pop()))
        return lists[0]


    def merge(self, a, b):
        dummy = ListNode(None)
        tail = dummy
        while a and b:
            if a.val < b.val:
                tail.next = a
                tail = tail.next
                a = a.next
            else:
                tail.next = b
                tail = tail.next
                b = b.next

        tail.next = a if a else b
        return dummy.next

s = Solution()
a = ListNode(0)
b = ListNode(1)
print b
s.mergeKLists([a,b])









