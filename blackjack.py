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
            return (str(self.cards[0]) + ' - ' + str(self.cards[0])[:-1] + ' points')
        else:
            return Player.__str__(self)

    def hit(self, deck):
        self.awaiting_hit = False
        while self.score() < 17:
            self.cards.append(deck.deal())

class Game(object):
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player = Player([self.deck.deal(), self.deck.deal()])
        self.dealer = Dealer([self.deck.deal(), self.deck.deal()])

    def play(self):
        print('Player: ' + str(self.player))
        print('Dealer: ' + str(self.dealer))

        while True:
            choice = input('\nHit or stay? (1 to hit, 2 to stay): ')
            if choice in ('h', 'H', 'hit', '1'):
                self.player.hit(self.deck.deal())
                print('Player: ' + str(self.player))
                if self.player.score() >= 21:
                    break
            else:
                break
        player_score = self.player.score()

        self.dealer.hit(self.deck)
        dealer_score = self.dealer.score()
        print('Dealer: ' + str(self.dealer))
        
        if player_score > 21:
            print('\nYou lose!')
        elif (dealer_score > 21) or Player.evaluate(self.player):
            print('\nYou win!')
        elif (dealer_score == 21) or Player.evaluate(self.dealer):
            if player_score == 21:
                print('\nIt\'s a tie!')
            else:
                print('\nYou lose!')
        elif dealer_score < 21:
            if player_score > dealer_score:
                print('\nYou win!')
            elif player_score < dealer_score:
                print('\nYou lose!')
            else:
                print('It\'s a tie!')

        choice = input('\nWould you like to play again? (y for yes, n for no): ')
        if choice in ('y', 'Y', 'yes'):
            blackjack =  Game()
            blackjack.play()

blackjack =  Game()
blackjack.play()