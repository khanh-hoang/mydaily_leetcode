#Time: O(N/k) where n all possible value, k : number of buckets
#Space:O(k+m) where m is number of unique value that inserted into set
class MyHashSet:

    def __init__(self):
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]
        
    def _hash(self, key):
        return key % self.keyRange
        
    def add(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)
        
    def remove(self, key: int) -> None:
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key: int) -> bool:
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)
    
    
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode
        
        
class Bucket: 
    def __init__(self):
        self.head = Node(0)
        
    def insert(self, newValue):
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            self.head.next = newNode
            
    def delete(self, value):
        prev = self.head
        cur = self.head.next
        while cur:
            if cur.value == value:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next
    
    def exists(self, value):
        cur = self.head.next
        while cur:
            if cur.value == value:
                return True
            cur = cur.next
        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)