#Time: O(1)
#Space:O(M) where M is size of incoming message
class Logger:

    def __init__(self):
        self.mymap = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.mymap:
            self.mymap[message] = timestamp
            return True
        else:
            if timestamp >= self.mymap[message] + 10:
                self.mymap[message] = timestamp
                return True
            else:
                return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)