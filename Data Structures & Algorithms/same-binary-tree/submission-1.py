# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q and p.val == q.val:
            return (True and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        elif p and q:
            return False
        elif p is None and q:
            return False
        elif q is None and p:
            return False
        else:
            return True