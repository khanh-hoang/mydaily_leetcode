#Time: O(n)
#Space:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        res = 0
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                if low <= node.val <= high:
                    res += node.val
                if low < node.val:
                    queue.append(node.left)
                if node.val < high:
                    queue.append(node.right)    
        return res
    
        """
        Dfs solution:
        self.res = 0
        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.res += node.val
                if low < node.val:
                    dfs(node.left)
                if node.val < right:
                    dfs(node.right)
        dfs(root)
        return self.res
        """