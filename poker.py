import string
import math
import random

class Card(object):
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    SUITS = ('C', 'D', 'H', 'S')

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        if self.rank == 1:
            rank = 'A'
        elif self.rank == 11:
            rank = 'J'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 13:
            rank = 'K'
        else:
            rank = self.rank
        return str(rank) + self.suit

class Deck(object):
    def __init__(self):
        self.deck = []
        for rank in Card.RANKS:
            for suit in Card.SUITS:
                self.deck.append(Card(rank, suit))
    
    def __len__(self):
        return len(self.deck)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        if len(self) > 0:
            return self.deck.pop(0)
        else:
            return None