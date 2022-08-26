# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ourmap = defaultdict(list)
        queue = deque([(root, 0)])
        mymin = mymax = 0
        while queue:
            node, col = queue.popleft()
            if node:
                ourmap[col].append(node.val)
                mymin = min(mymin, col)
                mymax = max(mymax, col)
                
                queue.append((node.left, col-1))
                queue.append((node.right, col+1))
        return [ourmap[x] for x in range(mymin, mymax+1)]
            
            
    