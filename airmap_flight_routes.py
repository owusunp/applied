"""
AirMap Flight Routes Problem

Implement a class called AirMap that has two methods:

1. add_route(start, destination)
   - adds a ONE WAY connecting flight from start to destination

2. print_all_routes(start, destination)
   - prints all possible routes from start to destination irrespective of hops

Sample inputs - Expected outputs:
Given the following flight routes, print all possible routes between the airports C and D

  A ----> B
  B ----> A
  A ----> C
  C ----> A
  A ----> D
  D ----> A
  B ----> C
  C ----> B
  B ----> D
  D ----> B

Expected output:
  C,A,B,D,
  C,A,D,
  C,B,A,D,

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Use DFS to find all possible paths between two airports.

**How it works**:
- Build a graph using adjacency list (dictionary)
- Use DFS to explore all possible paths from start to destination
- Keep track of current path to avoid cycles and print valid routes
- Use backtracking to explore all branches

**Key Points**:
- Use adjacency list to store one-way connections
- DFS explores all possible paths
- Track visited nodes to avoid cycles
- Backtrack when path doesn't lead to destination

**Example**: Find routes from C to D
- C → A → B → D (path: C,A,B,D)
- C → A → D (path: C,A,D)  
- C → B → A → D (path: C,B,A,D)

**Time Complexity**: O(V + E) where V is vertices and E is edges.
"""

from collections import defaultdict
from typing import List

class AirMap:
    def __init__(self):
        """
        Initialize AirMap with empty graph.
        """
        # Adjacency list to store one-way connections - graph representation
        self.graph = defaultdict(list)
    
    def add_route(self, start: str, destination: str) -> None:
        """
        Add a one-way flight route from start to destination.
        
        Args:
            start: Starting airport
            destination: Destination airport
        """
        # Add one-way connection to graph - store the route
        self.graph[start].append(destination)
    
    def print_all_routes(self, start: str, destination: str) -> None:
        """
        Print all possible routes from start to destination using DFS.
        
        Args:
            start: Starting airport
            destination: Destination airport
        """
        # Set to track visited airports in current path - prevent cycles
        visited = set()
        # Current path being explored - track the route
        current_path = []
        
        # DFS helper function to find all paths - explore all possible routes
        def dfs(current_airport, target_airport):
            # Add current airport to path and mark as visited - track current position
            current_path.append(current_airport)
            visited.add(current_airport)
            
            # If we reached the destination, print the path - found a valid route
            if current_airport == target_airport:
                # Print the path with commas - format the output
                print(','.join(current_path) + ',')
            else:
                # Explore all connected airports - try all possible next stops
                for next_airport in self.graph[current_airport]:
                    # Only visit if not already in current path - avoid cycles
                    if next_airport not in visited:
                        dfs(next_airport, target_airport)
            
            # Backtrack: remove from path and visited - allow other paths to use this airport
            current_path.pop()
            visited.remove(current_airport)
        
        # Start DFS from starting airport - begin path exploration
        dfs(start, destination)

# Test the AirMap implementation
if __name__ == "__main__":
    # Create AirMap instance - initialize the flight system
    airmap = AirMap()
    
    # Add all the flight routes - build the graph
    airmap.add_route("A", "B")
    airmap.add_route("B", "A") 
    airmap.add_route("A", "C")
    airmap.add_route("C", "A")
    airmap.add_route("A", "D")
    airmap.add_route("D", "A")
    airmap.add_route("B", "C")
    airmap.add_route("C", "B")
    airmap.add_route("B", "D")
    airmap.add_route("D", "B")
    
    print("All possible routes from C to D:")
    print("=" * 40)
    # Find and print all routes from C to D - solve the problem
    airmap.print_all_routes("C", "D")
