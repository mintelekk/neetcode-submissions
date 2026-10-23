
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        list1 = []
        countK = 0
        def dfs(node):
            nonlocal countK
            if not node is None:
                dfs(node.left)
                list1.append(node.val)
                countK += 1
                if countK == k:
                    return 0
                dfs(node.right)
        dfs(root)
        ans = list1[k-1]
        return ans