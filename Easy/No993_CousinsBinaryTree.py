#Time: O(n)
#Space:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque([root])
        while queue:
            sibling = False
            cousin = False
            
            for i in range(len(queue)):
                node = queue.popleft()
                if not node:
                    sibling = False
                else:
                    if node.val == x or node.val == y:
                        if not cousin:
                            sibling, cousin = True, True
                        else:
                            return not sibling
                    queue.append(node.left) if node.left else None
                    queue.append(node.right) if node.right else None
                    queue.append(None)
            if cousin:
                return False
        return False 