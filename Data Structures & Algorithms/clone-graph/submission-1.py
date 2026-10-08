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
            return None 

        nodeToClone = {} 

        def dfs(curr: Optional['Node']): 
            if curr in nodeToClone:   # base case checks if this node is already in the hashmap 
                return nodeToClone[curr] 
            else:
                nodeToClone[curr] = Node()
                nodeToClone[curr].val = curr.val 

                for neighbor in curr.neighbors: 
                    nodeToClone[curr].neighbors.append(dfs(neighbor))

                return nodeToClone[curr]

        return dfs(node)
            

