# Implements a cards shuffler and dealer.

import random

class Card:

    # initializes the card
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    # gives description of the card
    def description(self):
        return f"{self.value} of {self.suit}"

class Deck:

    # initializes the deck
    def __init__(self):
        self._cards = []
        self._suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        self._values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        for suit in self._suits:
            for value in self._values:
                card = Card(suit, value)
                self._cards.append(card)

    # gives a description of the deck
    def description(self):
        return f"{len(self._cards)} cards in the deck"\

    # shuffles the deck
    def shuffle(self):
        random.shuffle(self._cards)

    # removes and returns the top card of the deck
    def deal(self):
        return self._cards.pop((len(self._cards) - 1))

