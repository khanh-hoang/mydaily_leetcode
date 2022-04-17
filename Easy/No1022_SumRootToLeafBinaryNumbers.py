#Time: O(n)
#Space:O(H)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def preorder(node, cur_num):
            nonlocal res
            if node:
                cur_num = (cur_num << 1) | node.val
                if not node.left and not node.right:
                    res += cur_num
                preorder(node.left, cur_num)
                preorder(node.right, cur_num)
            
        res = 0
        preorder(root, 0)
        return res
                    
        """
        Time: O(n)
        Space:O(H)
        queue = deque([(root, "")])
        res = []
        while queue:
            node, val = queue.popleft()
            if not node.left and not node.right:
                res.append(val + str(node.val)) 
            if node.left:
                queue.append((node.left, val + str(node.val)))
            if node.right:
                queue.append((node.right, val + str(node.val)))
        return sum([int(i,2) for i in res])
        """