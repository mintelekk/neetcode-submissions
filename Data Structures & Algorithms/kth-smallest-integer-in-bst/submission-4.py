
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        list1 = []
        def dfs(node):
            if not node is None:
                dfs(node.left)
                list1.append(node.val)
                dfs(node.right)
        dfs(root)
        ans = list1[k-1]
        return ans