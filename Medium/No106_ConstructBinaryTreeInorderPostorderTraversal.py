#Time: O(n)
#Space:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(postorder.pop())
                root.right = build(root.val)
                inorder.pop()
                root.left = build(stop)
                return root
            
        return build(None)
        """
        mymap = {}
        for i, val in enumerate(inorder):
            mymap[val] = i
        
        def build(low, high):
            if low > high:
                return 
            x = TreeNode(postorder.pop())
            mid = mymap[x.val]
            x.right = build(mid + 1, high)
            x.left = build(low, mid - 1)
            return x
        
        return build(0, len(inorder)-1)
        """