# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = []
        ans = []
        if root is None:
            return ans
        queue.append(root)

        while queue:
            levelLength = len(queue)
            currentLevel = []
            for _ in range(levelLength):
                current = queue.pop(0)
                currentLevel.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            ans.append(currentLevel)
        return ans