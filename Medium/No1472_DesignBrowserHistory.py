#Time: O(1)
#Space:O(n)
class BrowserHistory:
    def __init__(self, homepage):
        self.history = [homepage]
        self.cur = 0
    
    def visit(self, url):
        self.cur += 1
        while self.cur < len(self.history):
            self.history.pop()
        self.history.append(url)
        
    def back(self, steps):
        self.cur = max(0, self.cur-steps)
        return self.history[self.cur]
    
    def forward(self, steps):
        self.cur = min(len(self.history)-1, self.cur + steps)
        return self.history[self.cur]

"""
class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = []
        self.future = []
        self.history.append(homepage)
        
    def visit(self, url:str):
        self.history.append(url)
        self.future = []
    
    def back(self, steps):
        while steps and len(self.history) > 1:
            self.future.append(self.history[-1])
            self.history.pop()
            steps -= 1
        return self.history[-1]
    
    def forward(self, steps):
        while steps and self.future:
            self.history.append(self.future[-1])
            self.future.pop()
            steps -= 1
        return self.history[-1]
            
"""
            
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None
    
class BrowserHistory:

    def __init__(self, homepage: str):
        self.root = ListNode(homepage)
        
    def visit(self, url: str) -> None:
        node = ListNode(url)
        node.prev = self.root
        self.root.next = node
        self.root = self.root.next

    def back(self, steps: int) -> str:
        while (steps and self.root.prev):
            self.root = self.root.prev
            steps -= 1
        return self.root.val

    def forward(self, steps: int) -> str:
        while (steps and self.root.next):
            self.root = self.root.next
            steps -= 1
        return self.root.val
"""


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)