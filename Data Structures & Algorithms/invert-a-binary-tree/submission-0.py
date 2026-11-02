# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # queue = deque([root])
        # if queue is None:
        #     return root
        # else:
        #     while queue:
        #         temp = queue.popleft()
        #         temp.left, temp.right = temp.right, temp.left
        #         if temp.left is not None:
        #             queue.append(temp.left)
        #         if temp.right is not None:
        #             queue.append(temp.right)
        #     return root

        if root == None:
            return root
        # queue = []
        # queue.append(root)
        queue = deque([root])


        while queue:
            temp = queue.popleft()
            #swap
            temp.left, temp.right = temp.right, temp.left

            if temp.left != None:
                queue.append(temp.left)
            if temp.right != None:
                queue.append(temp.right)
            
        return root

            