"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # List to store current substring without repeating characters
        result = []
        # Track the maximum length found so far
        best = 0

        # Iterate through each character in the string
        for i in s:
            # If character not in current substring, add it
            if i not in result:
                result.append(i)
            else:
                # Update best length before modifying substring
                best = max(best, len(result))
                # Remove characters up to and including the duplicate
                result = result[result.index(i) + 1:]
                # Add the current character to the end
                result.append(i)
            # Update best length after each character
            best = max(best, len(result))

        # Return the maximum length found
        return best
