"""
Connect 4 Game Status - Bloomberg Interview Question

Check the current status of Connect 4 game board and return:
1. If someone already wins (without any moves)
2. If one of the players can win with the next move

This is a harder version of LeetCode 794 (Valid Tic-Tac-Toe State).

THOUGHT PROCESS FOR INTERVIEWER:

The challenge is analyzing Connect 4 game states. Let me think through this:

1. **Problem Analysis**:
   - Check if current board has a winner
   - Check if next player can win in one move
   - Handle Connect 4 rules (4 in a row horizontally, vertically, or diagonally)

2. **Approach**:
   - **Check current winner**: Scan board for existing 4-in-a-row
   - **Check next move win**: Try all possible moves for next player
   - **Validate moves**: Ensure moves follow Connect 4 rules (gravity)

3. **Key Insights**: 
   - Connect 4 has gravity (pieces fall to bottom)
   - Need to check all 4 directions for wins
   - Only check valid moves (in empty columns)

4. **Example walkthrough**:
   - Board with 4 yellows in a row → Yellow wins
   - Board where next move creates 4-in-a-row → Next player can win

This gives us O(m*n) time complexity where m,n are board dimensions!
"""

from typing import List, Optional, Tuple

class Connect4Game:
    """
    Connect 4 game status checker.
    """
    
    def __init__(self):
        """
        Initialize the Connect 4 game checker.
        """
        self.directions = [
            (0, 1),   # Right
            (1, 0),   # Down
            (1, 1),   # Diagonal down-right
            (1, -1)   # Diagonal down-left
        ]
    
    def check_game_status(self, board: List[List[str]], next_player: str) -> str:
        """
        Check the current status of the Connect 4 game.
        
        Args:
            board: 2D array representing the game board
            next_player: Player who will make the next move ('R' or 'Y')
            
        Returns:
            Game status: 'R_wins', 'Y_wins', 'R_can_win', 'Y_can_win', or 'continue'
        """
        # Check if someone already won - check current board state
        current_winner = self._check_winner(board)  # Check for existing winner - scan board
        if current_winner:  # If someone already won - game is over
            return f"{current_winner}_wins"  # Return winner - game finished
        
        # Check if next player can win with one move - check next move possibility
        can_win = self._can_win_next_move(board, next_player)  # Check if next player can win - analyze possibilities
        if can_win:  # If next player can win - one move away
            return f"{next_player}_can_win"  # Return next player can win - one move away
        
        return "continue"  # Game continues - no immediate winner
    
    def _check_winner(self, board: List[List[str]]) -> Optional[str]:
        """
        Check if there's a current winner on the board.
        
        Args:
            board: 2D array representing the game board
            
        Returns:
            Winner ('R' or 'Y') or None if no winner
        """
        rows, cols = len(board), len(board[0])  # Get board dimensions - size of board
        
        # Check all positions for 4-in-a-row - scan entire board
        for row in range(rows):  # Check each row - iterate through rows
            for col in range(cols):  # Check each column - iterate through columns
                if board[row][col] != '.':  # If position is not empty - check occupied positions
                    winner = self._check_4_in_a_row(board, row, col)  # Check for 4-in-a-row - analyze position
                    if winner:  # If found 4-in-a-row - winner exists
                        return winner  # Return winner - game over
        
        return None  # No winner found - game continues
    
    def _check_4_in_a_row(self, board: List[List[str]], start_row: int, start_col: int) -> Optional[str]:
        """
        Check if there's a 4-in-a-row starting from the given position.
        
        Args:
            board: 2D array representing the game board
            start_row: Starting row position
            start_col: Starting column position
            
        Returns:
            Winner ('R' or 'Y') or None if no 4-in-a-row
        """
        player = board[start_row][start_col]  # Get player at position - current player
        rows, cols = len(board), len(board[0])  # Get board dimensions - size of board
        
        # Check all 4 directions for 4-in-a-row - analyze all possible lines
        for dr, dc in self.directions:  # Check each direction - iterate through directions
            count = 1  # Count consecutive pieces - start with 1 (current piece)
            
            # Check forward direction - count pieces in line
            for i in range(1, 4):  # Check next 3 positions - look ahead
                new_row, new_col = start_row + i * dr, start_col + i * dc  # Calculate new position - move in direction
                
                # Check bounds and matching piece - validate position and piece
                if (0 <= new_row < rows and 0 <= new_col < cols and 
                    board[new_row][new_col] == player):  # If position is valid and piece matches
                    count += 1  # Increment count - found matching piece
                else:  # If position is invalid or piece doesn't match - stop counting
                    break  # Stop checking this direction - no more matches
            
            # Check backward direction - count pieces in opposite direction
            for i in range(1, 4):  # Check previous 3 positions - look behind
                new_row, new_col = start_row - i * dr, start_col - i * dc  # Calculate new position - move opposite direction
                
                # Check bounds and matching piece - validate position and piece
                if (0 <= new_row < rows and 0 <= new_col < cols and 
                    board[new_row][new_col] == player):  # If position is valid and piece matches
                    count += 1  # Increment count - found matching piece
                else:  # If position is invalid or piece doesn't match - stop counting
                    break  # Stop checking this direction - no more matches
            
            if count >= 4:  # If found 4 or more in a row - winner found
                return player  # Return winner - game over
        
        return None  # No 4-in-a-row found - continue game
    
    def _can_win_next_move(self, board: List[List[str]], player: str) -> bool:
        """
        Check if the given player can win with their next move.
        
        Args:
            board: 2D array representing the game board
            player: Player to check ('R' or 'Y')
            
        Returns:
            True if player can win next move, False otherwise
        """
        rows, cols = len(board), len(board[0])  # Get board dimensions - size of board
        
        # Try each column for next move - check all possible moves
        for col in range(cols):  # Check each column - iterate through columns
            if board[0][col] == '.':  # If column is not full - valid move
                # Find row to place piece - gravity effect
                row = -1  # Initialize row - find landing position
                for r in range(rows - 1, -1, -1):  # Check from bottom to top - gravity
                    if board[r][col] == '.':  # If row is empty - found position
                        row = r  # Set row index - landing position
                        break  # Stop searching - found position
                
                if row != -1:  # If valid row found - can place piece
                    board[row][col] = player  # Place player piece - make move
                    
                    # Check if this move creates a win - analyze move result
                    if self._check_4_in_a_row(board, row, col):  # If move creates 4-in-a-row - winning move
                        board[row][col] = '.'  # Undo the move - restore board
                        return True  # Player can win - winning move found
                    
                    board[row][col] = '.'  # Undo the move - restore board
        
        return False  # No winning move found - cannot win next move
    
