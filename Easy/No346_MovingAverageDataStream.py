#Time: O(1)
#Space:O(n)
#Optimize sum by subtract tail and plus val
#Optimize len(queue) by use count
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.total = 0
        self.count = 0
    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        tail = self.queue.popleft() if self.count > self.size else 0   
        self.total = self.total - tail + val
        
        return self.total/len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)