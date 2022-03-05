#Time :O(n)
#Space:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        toList = []
        def dfs(node):
            if node:
                dfs(node.left)
                toList.append(node.val)
                dfs(node.right)
        dfs(root)
        
        left, right = 0, len(toList) - 1
        while left < right:
            if toList[left] + toList[right] == k:
                return True
            elif toList[left] + toList[right] < k:
                left += 1
            else:
                right -= 1
        return False