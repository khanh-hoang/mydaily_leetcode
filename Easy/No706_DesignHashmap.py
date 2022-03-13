#Time: O(N/k) where N: all possible keys, k = 2069 here
#Space:O(k+m) where m: number of unique keys
class MyHashMap:

    def __init__(self):
        self.space = 2069
        self.hash_map = [Bucket() for i in range(self.space)]
        
    def put(self, key: int, value: int) -> None:
        hash_key = key % self.space
        self.hash_map[hash_key].update(key, value)

    def get(self, key: int) -> int:
        hash_key = key % self.space
        return self.hash_map[hash_key].get(key)

    def remove(self, key: int) -> None:
        hash_key = key % self.space
        self.hash_map[hash_key].remove(key)
        
class Bucket:
    def __init__(self):
        self.bucket = []
    
    def get(self, key):
        for (k, v) in self.bucket:
            if k == key:
                return v
        return -1
    
    def update(self, key, value):
        found = False
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                self.bucket[i] = (key, value)
                found = True
                break
        
        if not found:
            self.bucket.append((key, value))
            
    def remove(self, key):
        for i, kv in enumerate(self.bucket):
            if key == kv[0]:
                del self.bucket[i]
        
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)