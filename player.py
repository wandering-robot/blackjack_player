from blackjack_cards import Deck, Card
from hands import Hand
from state import Q

from random import randint

class Player:
    def __init__(self,deck,agent,q=None):
        self.deck = deck
        self.agent = agent
        self.q = q

        self.hand = Hand(self.deck)
        self.cards = {}

        self.value = 0
        self.initialize_value()     #obtain value from either starting Q or card deal

        self.initial_action = None  
        self.initialize_action()    #set as either 0 or 1 as a boolean
    
    def __repr__(self):
        return f'{self.q}, value = {self.value}'

    def initialize_value(self):
        if self.q == None:
            for _ in range(2):
                card = self.deck.deal()
                self.value += card.value
                self.cards.update([card])
        else:
            self.value = self.q.value
            
    def initialize_action(self):
        if self.q == None:
            self.initial_action = randint(0,1)
        else:
            self.initial_action = self.q.action

            
if __name__ == "__main__":
    pass