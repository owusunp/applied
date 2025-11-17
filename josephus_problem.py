"""
Josephus Problem - Find the Winner

Given an array of length k, and a count of n. Write a code to find the winner 
as each person is eliminated if after n steps are taken from the start of the array, 
it lands on them. Last one left is the winner.

Example:
- Array: [1, 2, 3, 4, 5]
- Count: 3
- Process: Eliminate every 3rd person
- Winner: Last person remaining

THOUGHT PROCESS FOR INTERVIEWER:

The challenge is simulating the Josephus problem elimination process. Let me think through this:

1. **Problem Analysis**:
   - Start with k people in a circle
   - Count n steps and eliminate the person at that position
   - Continue until only one person remains
   - Return the winner (last person standing)

2. **Approach Options**:
   - **Simulation**: Use a list and remove elements - O(k*n)
   - **Mathematical formula**: Direct calculation - O(1)
   - **Simulation is clearer**: Easy to understand and implement

3. **Key Insight**: 
   - Use a list to represent people
   - Track current position and count steps
   - Remove eliminated person and continue
   - Last remaining person is the winner

4. **Example walkthrough with k=5, n=3**:
   - Start: [1, 2, 3, 4, 5], position=0
   - Count 3: eliminate 3, remaining: [1, 2, 4, 5], position=3
   - Count 3: eliminate 1, remaining: [2, 4, 5], position=1
   - Count 3: eliminate 5, remaining: [2, 4], position=1
   - Count 3: eliminate 2, remaining: [4], position=0
   - Winner: 4

This gives us O(k*n) time complexity where k = number of people!
"""

from typing import List

class Solution:
    def findWinner(self, k: int, n: int) -> int:
        """
        Find the winner using simulation approach.
        
        Args:
            k: Number of people (array length)
            n: Count of steps before elimination
            
        Returns:
            The winner (last person remaining)
        """
        # Create list of people - represent all participants
        people = list(range(1, k + 1))  # [1, 2, 3, ..., k] - all people in the game
        current_index = 0  # Start from first person - current position in circle
        
        # Continue until only one person remains - elimination process
        while len(people) > 1:  # Keep eliminating until one person left
            # Count n steps from current position - find person to eliminate
            current_index = (current_index + n - 1) % len(people)  # Calculate elimination position - wrap around circle
            eliminated_person = people.pop(current_index)  # Remove eliminated person - take them out of game
            # Note: current_index stays the same after pop because next person moves to current position
        
        return people[0]  # Return the last remaining person - the winner
    
    def findWinnerFormula(self, k: int, n: int) -> int:
        """
        Find the winner using mathematical formula (more efficient).
        
        Args:
            k: Number of people (array length)
            n: Count of steps before elimination
            
        Returns:
            The winner (last person remaining)
        """
        winner = 0  # Start with 0-based indexing - mathematical formula base case
        
        # Apply Josephus formula for each person - build solution bottom-up
        for i in range(1, k + 1):  # Calculate winner for 1, 2, 3, ..., k people
            winner = (winner + n) % i  # Josephus formula - mathematical relationship
        
        return winner + 1  # Convert to 1-based indexing - return actual person number
    
    def findWinnerDetailed(self, k: int, n: int) -> List[int]:
        """
        Find the winner and return elimination sequence.
        
        Args:
            k: Number of people (array length)
            n: Count of steps before elimination
            
        Returns:
            List showing elimination order
        """
        people = list(range(1, k + 1))  # Create list of people - all participants
        current_index = 0  # Start from first person - current position
        elimination_order = []  # Track elimination sequence - record who gets eliminated when
        
        # Continue until only one person remains - elimination process
        while len(people) > 1:  # Keep eliminating until one person left
            # Count n steps from current position - find person to eliminate
            current_index = (current_index + n - 1) % len(people)  # Calculate elimination position - wrap around circle
            eliminated_person = people.pop(current_index)  # Remove eliminated person - take them out of game
            elimination_order.append(eliminated_person)  # Record elimination - track who was eliminated
            # Note: current_index stays the same after pop because next person moves to current position
        
        return elimination_order + [people[0]]  # Return elimination order plus winner - complete sequence
