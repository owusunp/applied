from collections import deque

"""
So we're working with a 2D grid. Every cell in this grid can either be an open space that you can walk on, or it can be a mountain, which is impassable. On this grid, you're also given a set of coordinates that represent points of interest — think of them like keys or objectives you need to visit.

Your task is to choose a location somewhere on the grid to place a base camp. The base has to be on an open cell, not on a mountain. Once you place your base, you need to be able to reach every point of interest from that base. And there's an important constraint: every time you visit a point of interest, you must return back to the base before going to the next one. So you can't chain visits — it's always a round trip. Because of that, the cost of visiting any POI is just twice the shortest path distance from the base to that POI.

What we're trying to do is minimize the total fuel cost — which means picking the base location that results in the smallest sum of round-trip distances to all the points of interest. If a potential base can't reach all POIs because mountains block the way, then that base is invalid. And if no open cell can reach all of them, then we return something like [-1, -1]. Otherwise, we return the grid coordinates of the best base.

I have said enough here so I would stop
"""

# BFS to compute shortest distances from one starting point to all reachable open cells
def bfs(grid, start):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start[0], start[1], 0)])  # (row, col, dist)
    visited = set()
    visited.add((start[0], start[1]))
    distances = {}  # (r,c) -> distance

    while queue:
        r, c, dist = queue.popleft()

        # Record distances to open cells (bases can only be placed on open cells)
        if grid[r][c] == "":
            distances[(r, c)] = dist

        # Explore neighbors (up/down/left/right)
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < rows and 
                0 <= nc < cols and 
                (nr, nc) not in visited and 
                grid[nr][nc] != "#"
            ):
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return distances


def solve(grid: list[list[str]], points: list[list[int]]) -> list[int]:
    rows, cols = len(grid), len(grid[0])
    
    # Validate that all POIs are on open cells (not mountains)
    for r, c in points:
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "#":
            return [-1, -1]

    # Precompute BFS from each point of interest
    distances_from_poi = []
    for p in points:
        d = bfs(grid, p)
        distances_from_poi.append(d)

    best_cost = float("inf")
    best_base = [-1, -1]

    # Try every open cell as a potential base
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "":
                total_cost = 0
                reachable = True

                # Sum round-trip distances to every POI
                for d in distances_from_poi:
                    if (r, c) not in d:   # this base cannot reach this POI
                        reachable = False
                        break
                    dist = d[(r, c)]
                    total_cost += 2 * dist

                if reachable and total_cost < best_cost:
                    best_cost = total_cost
                    best_base = [r, c]

    return best_base


# ---------- Example Usage ----------

grid = [
  ["", "#", "", "", ""],
  ["", "#", "", "#", ""],
  ["", "", "", "", ""],
  ["", "", "", "#", ""],
  ["", "#", "", "", ""]
]

points = [[0, 4], [2, 0], [2, 4], [4, 3]]  # list of lists (keep as lists)

print(solve(grid, points))  # Expected: [2, 4]
