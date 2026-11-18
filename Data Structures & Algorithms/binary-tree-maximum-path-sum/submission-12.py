# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -1000
        
        def dfs(node):
            nonlocal result
            if node == None:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            result = max(result, (left+right+node.val))

            return node.val + max(left,right)
        
        dfs(root)
        
        return result  
        