#Time :O(1) for addHead
#      O(k) for addIndex, deleteIndex, get 
#      O(n)
#Space:O(1)
class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode()
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        cur = self.head
        
        for i in range(index+1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        if index < 0:
            index = 0
        
        self.size += 1
        pre = self.head
        for i in range(index):
            pre = pre.next
        
        add = ListNode(val)
        add.next = pre.next
        pre.next = add
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        
        self.size -= 1
        pre = self.head
        for i in range(index):
            pre = pre.next
        
        pre.next = pre.next.next
        
class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)