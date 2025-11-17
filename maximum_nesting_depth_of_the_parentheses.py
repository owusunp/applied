"""
Q1 - Substrings at Maximum Nesting Depth

Given a well-formed string s containing lowercase letters and square brackets [ ], return all substrings enclosed within brackets at the maximum nesting depth.

Example 1:
Input: s = "a[[vf]]md[d]m[a[sd]]"
Output: ["vf", "sd"]
Explanation: 
- "vf" is at depth 2 (inside [[vf]])
- "sd" is at depth 2 (inside [a[sd]])
- "d" is at depth 1 (inside [d])
- Maximum depth is 2, so we return ["vf", "sd"]

Example 2:
Input: s = "x[y[z]]w[a]b"
Output: ["z"]
Explanation:
- "z" is at depth 2 (inside [y[z]])
- "a" is at depth 1 (inside [a])
- Maximum depth is 2, so we return ["z"]

Constraints:
- 1 <= s.length <= 1000
- s contains only lowercase letters and square brackets
- The string is well-formed (all brackets are properly matched)

THOUGHT PROCESS FOR INTERVIEWER:

The challenge is finding all substrings at the maximum nesting depth. Let me think through this:

1. **Problem Analysis**:
   - Need to track current depth as we traverse the string
   - Increment depth when we see '['
   - Decrement depth when we see ']'
   - Collect substrings at maximum depth
   - Keep track of the maximum depth reached

2. **Approach**:
   - Use a counter to track current depth
   - Use a variable to track maximum depth
   - Use a list to collect substrings at max depth
   - Build current substring as we traverse

3. **Key Insight**: 
   - Each '[' increases depth by 1
   - Each ']' decreases depth by 1
   - Collect substrings when at maximum depth
   - Reset substring when depth changes

4. **Example walkthrough with s="a[[vf]]md[d]m[a[sd]]"**:
   - 'a', depth=0, current_substring="a"
   - '[', depth=1, current_substring=""
   - '[', depth=2, current_substring=""
   - 'v', depth=2, current_substring="v"
   - 'f', depth=2, current_substring="vf"
   - ']', depth=1, collect "vf" (depth=2 was max)
   - ']', depth=0, current_substring=""
   - Continue...

This gives us O(n) time complexity!
"""

class Solution:
    def maxDepthSubstrings(self, s: str) -> list:
        current_depth = 0  # Track current nesting depth - starts at 0 for no brackets
        max_depth = 0  # Track maximum depth reached - needed to find the deepest nesting
        result = []  # List to store substrings at maximum depth - our answer
        current_substring = ""  # Current substring being built - tracks content at current depth
        
        for char in s:  # Iterate through each character in the string
            if char == '[':  # Opening bracket increases depth - start of a new nested level
                current_depth += 1  # Increment current depth - we're going one level deeper
                max_depth = max(max_depth, current_depth)  # Update maximum depth if needed - track the deepest we've been
                current_substring = ""  # Reset substring for new depth level - start fresh content
            elif char == ']':  # Closing bracket decreases depth - end of current nested level
                if current_depth == max_depth and current_substring:  # If we're at max depth and have content - collect the substring
                    result.append(current_substring)  # Add substring to result - this is at maximum depth
                current_depth -= 1  # Decrement current depth - we're going back up one level
                current_substring = ""  # Reset substring for new depth level - start fresh content
            else:  # Regular character (lowercase letter) - add to current substring
                current_substring += char  # Build the substring at current depth - accumulate characters
        
        return result  # Return all substrings at maximum depth - the answer to the problem