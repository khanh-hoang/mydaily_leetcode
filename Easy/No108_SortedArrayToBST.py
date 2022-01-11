#Time: O(n)
#Space:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums or len(nums) == 0:
            return None 
        
        def bstrecursive(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            current = TreeNode(nums[mid])
            current.left = bstrecursive(left, mid-1)
            current.right = bstrecursive(mid + 1, right)
            return current 

        return bstrecursive(0, len(nums) -1 )
    