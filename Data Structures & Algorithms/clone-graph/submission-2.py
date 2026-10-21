"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return node 

        copyMap = {} 

        def dfs(curr) -> None:
            if curr in copyMap: 
                return copyMap[curr]

            newNode = Node(curr.val)
            copyMap[curr] = newNode 
            
            for neighbour in curr.neighbors:
                    newNode.neighbors.append(dfs(neighbour))

            return newNode

        return dfs(node)
