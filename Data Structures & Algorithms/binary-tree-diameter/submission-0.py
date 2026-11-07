# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root.left == None and root.right == None:
            return 0
        result = 0
        
        def traverse(node):
            nonlocal result
            if node == None:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            result = max(result, left + right)
            return 1 + max(left,right)
        
        traverse(root)
        
        return result

        