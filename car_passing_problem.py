"""
Car Passing Problem

Create a function taking a collection of integers representing the snapshot and returning the number of passings which will occur.

A value of 1 represents a west-bound car while 0 represents an east-bound car.
You may assume the data is sanitized and no other values will be present.

Example:
Input: [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0]
Output: Number of passings

THOUGHT PROCESS FOR INTERVIEWER:

The challenge is counting how many times west-bound cars (1) pass east-bound cars (0). Let me think through this:

1. **Problem Analysis**:
   - West-bound cars (1) are moving left (west)
   - East-bound cars (0) are moving right (east)
   - A passing occurs when a west-bound car is to the right of an east-bound car
   - We need to count all such pairs

2. **Approach**:
   - For each west-bound car (1), count how many east-bound cars (0) are to its left
   - Sum up all these counts

3. **Key Insight**: 
   - For each '1' at position i, count how many '0's are at positions < i
   - This gives us the number of passings for that west-bound car

4. **Example walkthrough with [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0]**:
   - Position 0: '1' - count '0's to the left: 0 (no '0's before position 0)
   - Position 2: '1' - count '0's to the left: 1 (one '0' at position 1)
   - Position 3: '1' - count '0's to the left: 1 (one '0' at position 1)
   - Position 5: '1' - count '0's to the left: 2 (two '0's at positions 1 and 4)
   - Position 8: '1' - count '0's to the left: 3 (three '0's at positions 1, 4, 6)
   - Position 9: '1' - count '0's to the left: 3 (three '0's at positions 1, 4, 6)
   - Total passings: 0 + 1 + 1 + 2 + 3 + 3 = 10

This gives us O(n²) time complexity!
"""

# Alternative optimized solution using prefix sum
def count_car_passings_optimized(cars):
    """
    Optimized version using prefix sum for O(n) time complexity.
    """
    # Count east-bound cars (0) at each position
    east_count = 0  # Count of east-bound cars seen so far - tracks east-bound cars to the left
    passings = 0  # Total number of passings - our answer
    
    for car in cars:  # Iterate through each car in the sequence
        if car == 0:  # If current car is east-bound (0) - increment east-bound counter
            east_count += 1  # Increment count of east-bound cars - track how many we've seen
        else:  # If current car is west-bound (1) - count passings with all east-bound cars to its left
            passings += east_count  # Add all east-bound cars to the left - each creates a passing
    
    return passings  # Return total number of passings - the answer to the problem
