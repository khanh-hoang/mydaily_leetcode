#Time: O(n) - O(1) for next and hasNext
#Space:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.store = []
        def dfs(node):
            if node:
                dfs(node.left)
                self.store.append(node.val)
                dfs(node.right)
         
        dfs(root)
        self.idx = -1
        
    
    
    def next(self) -> int:
        self.idx += 1
        return self.store[self.idx]

    def hasNext(self) -> bool:
        return self.idx + 1 < len(self.store)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()