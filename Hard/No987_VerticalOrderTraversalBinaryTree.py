# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = defaultdict(list)
        min_col = max_col = 0
        def bfs(root):
            nonlocal min_col, max_col
            queue = deque([(root, 0, 0)])
            while queue:
                node, row, col = queue.popleft()
                if node:
                    res[col].append((row, node.val))
                    min_col = min(min_col, col)
                    max_col = max(max_col, col)
                    
                    queue.append((node.left, row+1, col-1))
                    queue.append((node.right, row+1, col+1))
                    
        bfs(root)
        result = []
        for col in range(min_col, max_col+1):
            result.append([val for row, val in sorted(res[col])])
        print(res)
        return result