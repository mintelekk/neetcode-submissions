# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashMap1 = {}
        for i, v in enumerate(inorder):
            hashMap1[v] = i
        def build(left, right):
            if left > right:
                return None
            root_value = preorder.pop(0)
            root_index = hashMap1[root_value]
            root = TreeNode(root_value)
            root.left = build(left, root_index - 1)
            root.right = build(root_index + 1, right)
        
            return root
        return build(0, len(inorder) -1 )