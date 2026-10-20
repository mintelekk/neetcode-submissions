# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            #Base case: empty tree
            if node is None:
                return True, 0

            #DFS into both subtrees
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)


            #Current node is balanced if
            #both subtrees are balanced
            #their heights differ by at most 1
            balanced = (
                left_balanced
                and right_balanced
                and abs(left_height - right_height) <= 1
            )

            height = 1 + max(left_height, right_height)

            return balanced, height

        return dfs(root)[0]