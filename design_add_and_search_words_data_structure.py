"""
LeetCode #211 - Design Add and Search Words Data Structure

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

- WordDictionary() Initializes the object.
- void addWord(word) Adds word to the data structure, it can be matched later.
- bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example 1:
Input:
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output:
[null,null,null,null,false,true,true,true]

Constraints:
- 1 <= word.length <= 25
- word in addWord consists of lowercase English letters.
- word in search consist of '.' or lowercase English letters.
- At most 2 * 10^4 calls will be made to addWord and search.
"""

class TrieNode:
    def __init__(self):
        # Dictionary to store children nodes
        self.children = {}
        # Flag to mark end of word
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        # Initialize root as a TrieNode
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # Start from root node
        node = self.root
        # Navigate through each character in the word
        for c in word:
            # Create new node if character doesn't exist
            if c not in node.children:
                node.children[c] = TrieNode()
            # Move to the next level
            node = node.children[c]
        # Mark end of word
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # Helper function to perform DFS search
        def dfs(node, index):
            # Base case: if we've processed all characters
            if index == len(word):
                # Check if we're at the end of a complete word
                return node.is_end_of_word
            
            # Get current character
            char = word[index]
            
            # If character is '.', try all possible children
            if char == '.':
                # Check all children nodes
                for child in node.children.values():
                    # Recursively search from this child
                    if dfs(child, index + 1):
                        return True
                return False
            else:
                # If character exists, continue search
                if char in node.children:
                    return dfs(node.children[char], index + 1)
                # If character doesn't exist, word not found
                return False
        
        # Start DFS from root with index 0
        return dfs(self.root, 0)
