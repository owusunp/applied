"""
Second Question: Object Oriented Programming Style

Create a class that initializes a Training Data set that is meant to be used for autocomplete:

training_data = [
["I", "am", "Sam"],
["I", "Like", "ham"],
]

What data structure would you use to map each value to the count of the words that come after it ?

Write a function that checks the counts and predicts the most_likely word to come after a certain word?

House all of it in a proper class with initializers and what not

Extended training data:
training_data = [
["I", "am", "Sam"],
["I", "Like", "ham"],
["I", "am", "Bob"],
]

THOUGHT PROCESS FOR INTERVIEWER:

The challenge is building an autocomplete system using object-oriented programming. Let me think through this:

1. **Problem Analysis**:
   - Need to track which words follow each word
   - Count frequency of each follower
   - Find the most frequent follower for any given word

2. **Data Structure Choice**:
   - **Dictionary of dictionaries**: word -> {follower: count}
   - This allows O(1) lookup for followers and their counts
   - Easy to update frequencies

3. **Key Components**:
   - **Training function**: Parse sentences and build frequency map
   - **Frequency function**: Show all followers and their counts
   - **Prediction function**: Return most likely follower

4. **Example walkthrough with ["I", "am", "Sam"]**:
   - "I" -> "am" (count = 1)
   - "am" -> "Sam" (count = 1)
   - If we have ["I", "am", "bob"] too:
   - "I" -> "am" (count = 2)
   - "am" -> "Sam" (count = 1), "bob" (count = 1)

This gives us O(1) lookup time for predictions!
"""

from collections import defaultdict
from typing import List, Dict, Optional

class AutocompleteSystem:
    def __init__(self):
        # Initialize nested dictionary structure - word -> {follower: count} for O(1) lookup
        self.word_followers = defaultdict(lambda: defaultdict(int))
        # Track total words processed for statistics
        self.total_words = 0
    
    def train(self, training_data: List[List[str]]) -> None:
        # Process each sentence in the training data
        for sentence in training_data:
            # Skip sentences with less than 2 words - need at least 2 words for a follower relationship
            if len(sentence) < 2:
                continue
            
            # Iterate through each word except the last one - last word has no follower
            for i in range(len(sentence) - 1):
                # Get the current word - the word we're tracking followers for
                current_word = sentence[i]
                # Get the next word - the follower word
                next_word = sentence[i + 1]
                
                # Increment the count for this follower - track frequency
                self.word_followers[current_word][next_word] += 1
                # Increment total word count for statistics
                self.total_words += 1
    
    def predict_next_word(self, word: str) -> Optional[str]:
        # Check if word exists in our training data - no followers if not trained
        if word not in self.word_followers:
            return None
        
        # Get all followers for this word - retrieve the frequency map
        followers = self.word_followers[word]
        
        # Check if there are any followers - empty if no followers
        if not followers:
            return None
        
        # Get the word with maximum count - most frequent follower
        most_likely_word = max(followers, key=followers.get)
        # Return the most likely next word - our prediction
        return most_likely_word
    