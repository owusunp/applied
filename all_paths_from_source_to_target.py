"""
LeetCode #797 - All Paths From Source to Target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
find all possible paths from node 0 (source) to node n - 1 (target).

Example 1:
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Example 2:
Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

Constraints:
- n == graph.length
- 2 <= n <= 15
- 0 <= graph[i][j] < n
- graph[i][j] != i (i.e., the graph has no self-loops)
- All the elements of graph[i] are unique
- The input graph is guaranteed to be a DAG
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # Convert graph to defaultdict for safe access
        self.graph = collections.defaultdict(list)
        # Copy adjacency list to self.graph
        for i, edges in enumerate(graph):
            self.graph[i] = edges
        # List to store all valid paths found
        res = []
        
        def dfs(cur_path, cur_node):
            # Base case: reached target node (last node in graph)
            if cur_node == len(self.graph) - 1:
                # Add copy of current path to results
                res.append(list(cur_path))
                return
            
            # Explore all neighbors of current node
            for connection in self.graph[cur_node]:
                # Add neighbor to current path
                cur_path.append(connection)
                # Recursively explore from neighbor
                dfs(cur_path, connection)
                # Backtrack: remove neighbor to try other paths
                cur_path.pop()
        
        # Start DFS from source node 0 with initial path [0]
        dfs([0], 0)
        # Return all paths found
        return res
