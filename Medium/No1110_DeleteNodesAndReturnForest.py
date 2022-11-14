# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        queue = deque([(root, False)])
        res = []
        delete = set(to_delete)
        
        while queue:
            node, hasParent = queue.popleft()
            if not hasParent and not node.val in delete:
                res.append(node)
            hasParent = not node.val in delete
            
            if node.left:
                queue.append((node.left, hasParent))
                if node.left.val in delete:
                    node.left = None

            if node.right:
                queue.append((node.right, hasParent))
                if node.right.val in delete:
                    node.right = None
        return res
        
        """
        Time: O(n)
        Space:O(n)
        res = []
        
        def helper(root, is_root):
            if not root:
                return None
            root_deleted = root.val in to_delete
            if is_root and not root_deleted:
                res.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root
        helper(root, True)
        return res
        """
        