import string
import math
import random

class Card(object):
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades')

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
        return str(rank) + ' of ' + self.suit

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

class Player(object):
    def __init__(self, cards):
        self.cards = cards
    
    def __str__(self):
        hand = ''
        for num in range(len(self.cards)):
            hand += (str(self.cards[num]) + ' ')
        return (hand + ' - ' + str(self.score()) + ' points')
    
    def hit(self, card):
        self.cards.append(card)

    def score(self):
        count = 0
        for card in self.cards:
            if card.rank == 1:
                count += 11
            elif card.rank > 9:
                count += 10
            else:
                count += card.rank
        
        if count > 21:
            for card in self.cards:
                if card.rank == 1:
                    count -= 10

        return count
    
    def evaluate(self):
        return (len(self.cards) == 2) and (self.score() == 21)

class Dealer(Player):
    def __init__(self, cards):
        Player.__init__(self, cards)
        self.awaiting_hit = True
    
    def __str__(self):
        if self.awaiting_hit:
            return str(self.cards[0])
        else:
            return Player.__str__(self)

    def hit(self, deck):
        self.awaiting_hit = False
        while self.score() < 17:
            self.cards.append(deck.deal())

class Game(object):
    