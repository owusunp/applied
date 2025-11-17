"""
Candy Crush String Problem - Remove All Groups of 3 or More

You are given a string s. Remove all groups of 3 or more consecutive identical characters, then concatenate the remaining parts. Repeat this process until no more groups of 3+ can be removed.

You should greedily remove characters from left to right.

Return the final string after all such removals have been made.

Example 1:
Input: s = "aaaccccccbbbb"
Output: ""
Explanation: 
First remove "aaa" (3 a's) and "ccccc" (5 c's), get "bbbb"
Then remove "bbbb" (4 b's), get ""
Final result: ""

Example 2:
Input: s = "aaaccccccbbb"
Output: ""
Explanation: 
First remove "aaa" (3 a's) and "ccccc" (5 c's), get "bbb"
Then remove "bbb" (3 b's), get ""
Final result: ""

Example 3:
Input: s = "aaaccccccbb"
Output: "bb"
Explanation: 
Remove "aaa" (3 a's) and "ccccc" (5 c's), get "bb"
"bb" has only 2 b's, so no more crushing
Final result: "bb"

Constraints:
- 1 <= s.length <= 10^5
- s only contains lowercase English letters.

THOUGHT PROCESS FOR INTERVIEWER:

The challenge is removing all groups of 3+ consecutive duplicates and handling cascading effects.
 Let me think through this:

1. **Problem Analysis**: 
   - Remove ALL groups of 3+ adjacent identical characters
   - After removal, new adjacent duplicates may form
   - Need to handle cascading removals until stable

2. **Approach Options**:
   - **Brute force**: Repeatedly scan and remove - O(n²) time
   - **Single stack approach**: Track consecutive counts and remove immediately - O(n) time
   - **Single stack is optimal**: One pass, handles cascading naturally

3. **Key Insight**: Use single stack to track [character, count] pairs
   - When same character: increment count
   - When count reaches 3+: immediately remove from stack
   - This naturally handles cascading because removing creates new adjacencies

4. **Example walkthrough with s="aaaccccccbbbb"**:
   - 'a': stack=[['a',1]]
   - 'a': stack=[['a',2]]
   - 'a': stack=[['a',3]] → remove → stack=[]
   - 'c': stack=[['c',1]]
   - 'c': stack=[['c',2]]
   - 'c': stack=[['c',3]] → remove → stack=[]
   - 'c': stack=[['c',1]]
   - 'c': stack=[['c',2]]
   - 'c': stack=[['c',3]] → remove → stack=[]
   - 'b': stack=[['b',1]]
   - 'b': stack=[['b',2]]
   - 'b': stack=[['b',3]] → remove → stack=[]
   - 'b': stack=[['b',1]]
   - Result: "b"

This gives us O(n) time complexity with single pass!
"""

class Solution:
    def candyCrush(self, s: str) -> str:
        # Single stack approach - O(n) time, O(n) space
        # Keep processing until no more groups of 3+ can be removed
        while True:
            # Stack stores [character, count] pairs to track consecutive duplicates
            stack = []
            
            # Process each character in the string
            for char in s:
                # If stack is not empty and current character matches the top character
                if stack and stack[-1][0] == char:
                    # Increment the count of the top character
                    stack[-1][1] += 1
                else:
                    # Add new character with count 1
                    stack.append([char, 1])
            
            # Remove all groups of 3+ from stack and reconstruct string
            new_s = ""
            for char, count in stack:
                if count < 3:
                    new_s += char * count
            
            # If no changes were made, we're done
            if new_s == s:
                break
            
            # Update string for next iteration
            s = new_s
        
        return s

if __name__ == "__main__":
    sol = Solution()
    
    print("=== EXAMPLE 2: 'aaaccccccbbb' ===")
    result = sol.candyCrush('aaaccccccbbb')
    print(f"\nExpected: ''")
    print(f"Actual: '{result}'")
    print(f"Match: {result == ''}")