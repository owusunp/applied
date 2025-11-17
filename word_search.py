"""
LeetCode #79 - Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.

THOUGHT PROCESS FOR INTERVIEWER:

The challenge is finding a word in a 2D grid using DFS with backtracking. Let me think through this:

1. **Problem Analysis**:
   - Need to find a word by connecting adjacent cells
   - Can only move horizontally or vertically
   - Cannot reuse the same cell
   - Need to check all possible starting positions

2. **Approach**:
   - **DFS with Backtracking**: Explore all possible paths
   - **Start from each cell**: Try every position as starting point
   - **Track visited cells**: Prevent reusing same cell
   - **Backtrack**: Remove cell from visited when returning

3. **Key Insight**: 
   - Use DFS to explore all 4 directions from each cell
   - Mark cells as visited during exploration
   - Backtrack by removing from visited set
   - Return True as soon as word is found

4. **Example walkthrough with board=[["A","B"],["C","D"]], word="AB"**:
   - Start at (0,0): 'A' matches word[0], explore 4 directions
   - Move to (0,1): 'B' matches word[1], found complete word
   - Return True

This gives us O(m*n*4^L) time complexity where L = word length!
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Find if word exists in the board using DFS with backtracking.
        
        Example walkthrough with board=[["A","B","C"],["S","F","C"]], word="ABF":
        - Try starting at (0,0): 'A' matches word[0]
          - Explore (0,1): 'B' matches word[1] 
            - Explore (1,1): 'F' matches word[2] → Found word!
        - Return True
        
        Args:
            board: 2D grid of characters
            word: Word to search for
            
        Returns:
            True if word exists, False otherwise
        """
        # Get dimensions of the board - size of grid
        rows, cols = len(board), len(board[0])
        # Set to track visited cells (prevents reusing same cell) - avoid cycles
        path = set()
        
        def dfs(r, c, i):
            """
            DFS function to explore all possible paths from current position.
            
            Args:
                r, c: Current row and column position
                i: Current index in the word we're searching for
                
            Returns:
                True if word can be found from this position, False otherwise
            """
            # Base case: if we've found all letters in the word - success condition
            if i == len(word):
                return True  # Word found - return success
            
            # Check bounds, letter match, and if cell already visited - validation
            if (r < 0 or c < 0 or r >= rows or c >= cols or 
                word[i] != board[r][c] or (r, c) in path):
                return False  # Invalid position or already visited - backtrack
            
            # Mark current cell as visited - prevent revisiting
            path.add((r, c))
            
            # Explore all 4 directions (up, down, left, right) recursively - try all paths
            res = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
            
            # Backtrack: remove current cell from visited set - allow other paths to use this cell
            path.remove((r, c))
            
            # Return result (True if any direction found the word) - propagate success
            return res
        
        # Scan entire board for starting positions - try every cell as starting point
        for r in range(rows):  # Check each row - iterate through rows
            for c in range(cols):  # Check each column - iterate through columns
                # Start DFS from each cell (DFS checks if first letter matches) - try all starting positions
                if dfs(r, c, 0):  # If word found starting from this position - success
                    return True  # Return True as soon as word is found - early termination
        
        # Return False if word not found anywhere - no valid path exists
        return False
