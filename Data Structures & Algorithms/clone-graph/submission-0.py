"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        def dfs(original):
            if original in old_to_new:
                return old_to_new[original]

            clone = Node(original.val)
            old_to_new[original] = clone
            for neighbor in original.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone
        if node == None:
            return None
        if len(node.neighbors) == 0:
            return Node()
        node1 = dfs(node)
        return node1