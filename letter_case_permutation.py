"""
LeetCode #784: Letter Case Permutation

Given a string s, you can transform every letter individually to be lowercase or uppercase 
to create another string.

Return a list of all possible strings we could create. Return the output in any order.

Example 1:
Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

Example 2:
Input: s = "3z4"
Output: ["3z4","3Z4"]

Example 3:
Input: s = "C"
Output: ["c","C"]

Constraints:
- 1 <= s.length <= 12
- s consists of lowercase English letters, uppercase English letters, and digits.

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Use backtracking to explore all possible combinations.

**Key Insight**: 
At each letter, we have 2 choices: lowercase or uppercase.
At each digit, we have 1 choice: keep it as is.

**How it works**:
- Start with an empty path
- For each character in the string:
  - If it's a digit: add it to path and move to next
  - If it's a letter: try both lowercase and uppercase versions
- When we reach the end, we have one complete permutation

**Example**: s = "a1b"
- Start: ""
- Position 0 (letter 'a'): Try 'a' and 'A'
  - Path 'a': move to position 1
    - Position 1 (digit '1'): add '1', move to position 2
      - Position 2 (letter 'b'): Try 'b' and 'B'
        - Path 'a1b': complete ✓
        - Path 'a1B': complete ✓
  - Path 'A': move to position 1
    - Position 1 (digit '1'): add '1', move to position 2
      - Position 2 (letter 'b'): Try 'b' and 'B'
        - Path 'A1b': complete ✓
        - Path 'A1B': complete ✓

Result: ["a1b", "a1B", "A1b", "A1B"]

**Time**: O(2^n × n) where n is number of letters (2 choices per letter, n to build each string)
**Space**: O(2^n × n) for storing all permutations
"""

from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        """
        Generate all letter case permutations using backtracking.
        
        Args:
            s: Input string with letters and digits
            
        Returns:
            List of all possible permutations
        """
        result = []
        
        def backtrack(index: int, path: str):
            """
            Backtrack to build all permutations.
            
            Args:
                index: Current position in string - tells us which character to process
                path: Current permutation being built - accumulates our choices
            """
            # Base case: reached end of string, we have a complete permutation
            # Add it to results and return to explore other paths
            if index == len(s):
                result.append(path)
                return
            
            # Get current character to process
            char = s[index]
            
            # Case 1: Character is a digit (0-9)
            # Only one choice: keep it as is and move to next position
            if char.isdigit():
                backtrack(index + 1, path + char)
            
            # Case 2: Character is a letter (a-z or A-Z)
            # Two choices: lowercase and uppercase
            else:
                # Choice 1: Add lowercase version
                # We explore this branch first, then backtrack to try uppercase
                backtrack(index + 1, path + char.lower())
                
                # Choice 2: Add uppercase version
                # After exploring lowercase branch, we try uppercase
                backtrack(index + 1, path + char.upper())
        
        # Start backtracking from index 0 with empty path
        backtrack(0, "")
        return result
    
    def letterCasePermutationIterative(self, s: str) -> List[str]:
        """
        Generate all letter case permutations using iterative approach.
        
        **Approach**: 
        Start with one permutation (the original string).
        For each letter we encounter, double our permutations:
        - Keep existing ones as is
        - Create duplicates and toggle that letter's case
        
        **Example**: s = "a1b"
        - Start: ["a1b"]
        - Position 0 (letter 'a'): 
          - Keep: ["a1b"]
          - Duplicate & toggle: ["A1b"]
          - Result: ["a1b", "A1b"]
        - Position 1 (digit '1'): Skip (no change)
          - Result: ["a1b", "A1b"]
        - Position 2 (letter 'b'):
          - Keep: ["a1b", "A1b"]
          - Duplicate & toggle: ["a1B", "A1B"]
          - Result: ["a1b", "A1b", "a1B", "A1B"]
        
        Args:
            s: Input string with letters and digits
            
        Returns:
            List of all possible permutations
        """
        # Start with one permutation - the original string converted to list for mutability
        # We use list because strings are immutable in Python
        result = [[char for char in s]]
        
        # Process each character position
        for i in range(len(s)):
            # Only process if current character is a letter
            # Digits don't create new permutations
            if s[i].isalpha():
                # Get current number of permutations before doubling
                # We need this because we're adding to result while iterating
                n = len(result)
                
                # For each existing permutation, create a duplicate with toggled case
                for j in range(n):
                    # Create a copy of current permutation
                    # We copy because we want to modify without affecting original
                    new_perm = result[j][:]
                    
                    # Toggle the case at position i
                    # swapcase() converts 'a' to 'A' and 'A' to 'a'
                    new_perm[i] = new_perm[i].swapcase()
                    
                    # Add the new permutation to results
                    # Now we have 2x permutations (original + toggled)
                    result.append(new_perm)
        
        # Convert each list back to string before returning
        # Join characters in each permutation to form strings
        return [''.join(perm) for perm in result]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    print("=== Letter Case Permutation Tests ===")
    print()
    
    # Test case 1
    s1 = "a1b2"
    result1 = solution.letterCasePermutation(s1)
    print(f"Test 1:")
    print(f"Input: '{s1}'")
    print(f"Output: {result1}")
    print(f"Expected: ['a1b2','a1B2','A1b2','A1B2']")
    print()
    
    # Test case 2
    s2 = "3z4"
    result2 = solution.letterCasePermutation(s2)
    print(f"Test 2:")
    print(f"Input: '{s2}'")
    print(f"Output: {result2}")
    print(f"Expected: ['3z4','3Z4']")
    print()
    
    # Test case 3
    s3 = "C"
    result3 = solution.letterCasePermutation(s3)
    print(f"Test 3:")
    print(f"Input: '{s3}'")
    print(f"Output: {result3}")
    print(f"Expected: ['c','C']")
    print()
    
    # Test case 4
    s4 = "12345"
    result4 = solution.letterCasePermutation(s4)
    print(f"Test 4 (all digits):")
    print(f"Input: '{s4}'")
    print(f"Output: {result4}")
    print(f"Expected: ['12345']")
    print()
    
    # Test case 5
    s5 = "ab"
    result5 = solution.letterCasePermutation(s5)
    print(f"Test 5:")
    print(f"Input: '{s5}'")
    print(f"Output: {result5}")
    print(f"Expected: ['ab','aB','Ab','AB']")
    print()
