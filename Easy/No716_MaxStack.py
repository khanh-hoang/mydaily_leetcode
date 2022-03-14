#Time :O(n) for popMax, O(1) for the rest
#Space:O(n)
class MaxStack:

    def __init__(self):
        self.stack = []
        self.maxStack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.maxStack:
            self.maxStack.append(x)
        else:
            curMax = self.peekMax()
            self.maxStack.append(max(x, curMax))
            
    def pop(self) -> int:
        self.maxStack.pop()
        return self.stack.pop()
            
    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.maxStack[-1]

    def popMax(self) -> int:
        tempMax, tempList = self.peekMax(), []
        cur = self.pop()
        while cur != tempMax:
            tempList.append(cur)
            cur = self.pop()
        
        while tempList:
            self.push(tempList.pop())
        return tempMax
        
# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()