"""
Deck of Cards - Design Classes

Design a deck of cards with proper classes for Card and Deck.
Include methods to shuffle the deck.

THOUGHT PROCESS FOR INTERVIEWER:

The challenge is designing a proper deck of cards system. Let me think through this:

1. **Problem Analysis**:
   - Need Card class to represent individual cards
   - Need Deck class to manage collection of cards
   - Cards have ranks (A, 2-10, J, Q, K) and suits (Hearts, Diamonds, Clubs, Spades)
   - Need shuffle functionality

2. **Class Design**:
   - **Card class**: rank, suit, value for comparison
   - **Deck class**: collection of cards, shuffle method
   - **Encapsulation**: proper data hiding and methods

3. **Key Components**:
   - **Card**: rank, suit, value
   - **Deck**: cards list, shuffle method
   - **Shuffle**: randomize card order

4. **Example walkthrough**:
   - Create deck with 52 cards
   - Shuffle to randomize order
   - Deal cards from deck

This gives us a clean OOP design for card games!
"""

import random
from typing import List, Optional

class Card:
    """
    Represents a single playing card with rank and suit.
    """
    
    def __init__(self, rank: str, suit: str):
        """
        Initialize a card with rank and suit.
        
        Args:
            rank: Card rank (A, 2-10, J, Q, K)
            suit: Card suit (Hearts, Diamonds, Clubs, Spades)
        """
        self.rank = rank  # Store card rank - the number or face value
        self.suit = suit  # Store card suit - the symbol/color
        self.value = self._get_value()  # Calculate numeric value - for comparison and scoring
    
    def _get_value(self) -> int:
        """
        Get numeric value of card for comparison.
        
        Returns:
            Numeric value of the card
        """
        if self.rank == 'A':  # Ace is highest - special case for ace
            return 14  # Ace value - highest card
        elif self.rank in ['J', 'Q', 'K']:  # Face cards - jack, queen, king
            face_values = {'J': 11, 'Q': 12, 'K': 13}  # Face card values - mapping
            return face_values[self.rank]  # Return face card value - specific value
        else:  # Number cards - 2 through 10
            return int(self.rank)  # Return numeric value - direct conversion
    
    def __str__(self) -> str:
        """
        String representation of the card.
        
        Returns:
            Formatted string of the card
        """
        return f"{self.rank} of {self.suit}"  # Return readable card description - user-friendly format
    
    def __repr__(self) -> str:
        """
        Developer representation of the card.
        
        Returns:
            Developer-friendly string of the card
        """
        return f"Card('{self.rank}', '{self.suit}')"  # Return code representation - for debugging
    
    def __eq__(self, other) -> bool:
        """
        Check if two cards are equal.
        
        Args:
            other: Another card to compare
            
        Returns:
            True if cards are equal, False otherwise
        """
        if not isinstance(other, Card):  # Check if other is a Card - type validation
            return False  # Not a card - not equal
        return self.rank == other.rank and self.suit == other.suit  # Compare rank and suit - equality check
    
    def __lt__(self, other) -> bool:
        """
        Check if this card is less than another card.
        
        Args:
            other: Another card to compare
            
        Returns:
            True if this card is less than other, False otherwise
        """
        if not isinstance(other, Card):  # Check if other is a Card - type validation
            return False  # Not a card - not comparable
        return self.value < other.value  # Compare numeric values - less than comparison

class Deck:
    """
    Represents a deck of playing cards with shuffle functionality.
    """
    
    def __init__(self):
        """
        Initialize a standard 52-card deck.
        """
        self.cards = []  # Initialize empty deck - start with no cards
        self._create_deck()  # Build standard deck - create all 52 cards
    
    def _create_deck(self) -> None:
        """
        Create a standard 52-card deck.
        """
        ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']  # All card ranks - from ace to king
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']  # All card suits - four suits
        
        # Create all 52 cards - generate complete deck
        for suit in suits:  # For each suit - iterate through all suits
            for rank in ranks:  # For each rank in current suit - iterate through all ranks
                card = Card(rank, suit)  # Create new card - instantiate card object
                self.cards.append(card)  # Add card to deck - build collection
    
    def shuffle(self) -> None:
        """
        Shuffle the deck to randomize card order.
        """
        random.shuffle(self.cards)  # Randomize card order - shuffle the deck
    
    def deal_card(self) -> Optional[Card]:
        """
        Deal one card from the top of the deck.
        
        Returns:
            Card from top of deck, or None if deck is empty
        """
        if self.cards:  # If deck has cards - check if not empty
            return self.cards.pop(0)  # Remove and return top card - deal from top
        return None  # No cards left - deck is empty
    
    def deal_cards(self, num_cards: int) -> List[Card]:
        """
        Deal multiple cards from the deck.
        
        Args:
            num_cards: Number of cards to deal
            
        Returns:
            List of cards dealt
        """
        dealt_cards = []  # Initialize empty list - store dealt cards
        
        # Deal requested number of cards - get cards from deck
        for _ in range(num_cards):  # Deal specified number of cards - iterate through count
            card = self.deal_card()  # Deal one card - get card from deck
            if card:  # If card was dealt - check if not None
                dealt_cards.append(card)  # Add card to dealt list - collect cards
            else:  # No more cards - deck is empty
                break  # Stop dealing - no more cards available
        
        return dealt_cards  # Return all dealt cards - complete hand
    
    def add_card(self, card: Card) -> None:
        """
        Add a card to the deck.
        
        Args:
            card: Card to add to deck
        """
        self.cards.append(card)  # Add card to bottom of deck - insert card
    
    def size(self) -> int:
        """
        Get the number of cards in the deck.
        
        Returns:
            Number of cards remaining in deck
        """
        return len(self.cards)  # Return deck size - count remaining cards
    
    def is_empty(self) -> bool:
        """
        Check if the deck is empty.
        
        Returns:
            True if deck is empty, False otherwise
        """
        return len(self.cards) == 0  # Check if no cards left - empty deck
    
    def __str__(self) -> str:
        """
        String representation of the deck.
        
        Returns:
            Formatted string of the deck
        """
        return f"Deck with {len(self.cards)} cards"  # Return deck description - user-friendly format
    
    def __repr__(self) -> str:
        """
        Developer representation of the deck.
        
        Returns:
            Developer-friendly string of the deck
        """
        return f"Deck({len(self.cards)} cards)"  # Return code representation - for debugging
