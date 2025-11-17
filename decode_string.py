"""
LeetCode #394 - Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:
- 1 <= s.length <= 30
- s consists of lowercase English letters, digits, and characters '[' and ']'.
- s is a valid encoded string, that is, s will always have a corresponding closing bracket ']' for every opening bracket '['.
- The encoded string will not be empty.

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Use a stack to handle nested brackets and build the result step by step.

**How it works**:
- When we see a digit, we build the number (could be multi-digit)
- When we see '[', we save our current string and number to the stack
- When we see ']', we pop from stack and repeat the current string
- When we see a letter, we add it to our current string

**Key Points**:
- Stack stores [previous_string, repeat_count] pairs
- Handle multi-digit numbers by building them character by character
- When we see ']', repeat current string and combine with previous string
- Keep track of current string being built

**Example**: s="3[a2[c]]"
- Process '3': number = 3
- Process '[': stack = [[], 3], current = ""
- Process 'a': current = "a"
- Process '2': number = 2
- Process '[': stack = [[], 3, "a", 2], current = ""
- Process 'c': current = "c"
- Process ']': repeat "c" 2 times = "cc", combine with "a" = "acc"
- Process ']': repeat "acc" 3 times = "accaccacc"

**Time Complexity**: O(n) where n is the length of the decoded string.
"""

class Solution:
    def decodeString(self, s: str) -> str:
        """
        Decode the encoded string using stack to handle nested brackets.
        
        Args:
            s: Encoded string with k[encoded_string] pattern
            
        Returns:
            Decoded string
        """
        # Stack to store [previous_string, repeat_count] pairs - handle nested brackets
        stack = []
        # Current string being built - what we're working on right now
        current_string = ""
        # Current number being built - could be multi-digit like 12
        current_number = 0
        
        # Process each character in the string - go through input one by one
        for char in s:
            # If character is a digit, build the number - handle multi-digit numbers
            if char.isdigit():
                # Multiply by 10 to shift digits left, add current digit - build number digit by digit
                current_number = current_number * 10 + int(char)
            # If character is opening bracket, save current state to stack - start of new nested section
            elif char == '[':
                # Save current string and number to stack - preserve state before entering nested section
                stack.append([current_string, current_number])
                # Reset for new nested section - start fresh inside brackets
                current_string = ""
                current_number = 0
            # If character is closing bracket, repeat current string and combine - end of nested section
            elif char == ']':
                # Get previous string and repeat count from stack - restore previous state
                prev_string, repeat_count = stack.pop()
                # Repeat current string and combine with previous - build the result
                current_string = prev_string + current_string * repeat_count
            # If character is a letter, add to current string - regular character
            else:
                # Add letter to current string being built - accumulate characters
                current_string += char
        
        # Return the final decoded string - result after processing all characters
        return current_string




