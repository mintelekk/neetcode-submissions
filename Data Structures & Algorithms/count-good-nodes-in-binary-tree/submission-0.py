# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, runningMax):
            count = 0 
            if node is None:
                return 0
            if node.val >= runningMax:
                count = 1
                runningMax = node.val
            return count + dfs(node.left, runningMax) + dfs(node.right, runningMax)
        return dfs(root, -101)