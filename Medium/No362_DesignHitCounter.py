#Time: O(s) with s = 300 for getHits
#Space:O(s)
class HitCounter:

    def __init__(self):
        self.range = 300 
        self.times = [0] * self.range
        self.hits = [0] * self.range
        
    def hit(self, timestamp):
        idx = timestamp % self.range
        if timestamp != self.times[idx]:
            self.times[idx] = timestamp
            self.hits[idx] = 1
        else:
            self.hits[idx] += 1
    
    def getHits(self, timestamp):
        res = 0
        for i in range(self.range):
            if timestamp - self.times[i] < self.range:
                res += self.hits[i]
        return res
    
    """
    def __init__(self):
        self.counter = defaultdict(int)
    def hit(self, timestamp: int) -> None:
        self.counter[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        res = 0
        for k, v in self.counter.items():
            if k >= timestamp - 300 + 1 and k <= timestamp + 1:
                res += v
        return res            

    """

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)