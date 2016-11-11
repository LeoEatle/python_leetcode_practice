class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def addNext(self, val):
        self.next = ListNode(val)

    def show(self):
        head = self
        while not head == None:
            print head.val
            head = head.next
