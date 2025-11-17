"""
Word Break - Return One Segmentation

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where 
each word is a valid dictionary word. Return ONE such possible sentence.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: "cats and dog" (or "cat sand dog" - any valid segmentation)

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: "pine apple pen apple" (or any other valid segmentation)

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: "" (empty string if no valid segmentation)

Constraints:
- 1 <= s.length <= 20
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 10
- s and wordDict[i] consist of only lowercase English letters.
- All the strings of wordDict are unique.

THOUGHT PROCESS FOR INTERVIEWER:

**Approach**: Dynamic Programming - solve subproblems and combine solutions.

**What is DP here**:
- Break problem into smaller subproblems (valid sentences for prefixes)
- Store solutions to subproblems in dp array to avoid recomputation
- Build solution bottom-up by combining smaller solutions
- dp[i] stores one valid sentence for the first i characters

**Key Points**:
- dp[i] = one valid sentence for first i characters
- For each position i, check all possible starting positions j before i
- If word from j to i exists and dp[j] is valid, extend the sentence
- Return first valid segmentation found

**Example**: s="catsanddog", wordDict=["cat","cats","and","sand","dog"]
- dp[3] = "cat" (word "cat" ends at position 3)
- dp[4] = "cats" (word "cats" ends at position 4) 
- dp[7] = "cat sand" (extend "cat" with "sand")
- dp[10] = "cat sand dog" (extend with "dog")

**Time Complexity**: O(n²) - for each position i, check all starting positions j before i.
"""

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> str:
        """
        Find one way to segment string into dictionary words using dynamic programming.
        
        Args:
            s: Input string to segment
            wordDict: List of valid words
            
        Returns:
            One valid segmented sentence, or empty string if no segmentation exists
        """
        word_set = set(wordDict)  # Convert to set for O(1) lookup - faster than list lookup
        
        # DP array: dp[i] contains one valid sentence for s[0:i] - track one segmentation
        dp = [""] * (len(s) + 1)  # Initialize empty strings for each position
        dp[0] = ""  # Empty string - base case for DP
        
        # Build DP array bottom-up - find one valid segmentation
        for i in range(1, len(s) + 1):  # Check each possible end position
            for j in range(i):  # Check all possible start positions before i
                word = s[j:i]  # Extract substring - current word candidate
                
                # If substring is valid word and previous part has segmentation - valid combination
                if word in word_set and (j == 0 or dp[j] != ""):  # If word exists and (start or previous part is segmentable)
                    # Combine previous segmentation with current word - build one sentence
                    if j == 0:  # If this is the first word - no space needed
                        dp[i] = word
                    else:  # If previous sentence exists - combine with space
                        dp[i] = dp[j] + " " + word
                    break  # Stop after finding first valid segmentation - we only need one
        
        return dp[len(s)]  # Return one valid segmentation of entire string - final answer