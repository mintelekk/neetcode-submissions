def isSameTree(p, q):
    if not p and not q:
        return True
    if p and q and p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    return False

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def bfs(node):
            if node is None:
                return False
            elif node.val == subRoot.val:
                return isSameTree(node, subRoot) or bfs(node.left) or bfs(node.right)
            else:
                return bfs(node.left) or bfs(node.right)


        return bfs(root)