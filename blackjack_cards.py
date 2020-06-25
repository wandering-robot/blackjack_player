import random as r

class Deck:
    def __init__(self):
        self.pos_nums = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.pos_suites = ['S','H','C','D']
        
        self.cards = self.create_deck()
        self.shuffle()

    def create_deck(self):
        cards = []
        for suite in self.pos_suites:
            for num in self.pos_nums:
                cards.append(Card(num,suite))
        return cards

    def shuffle(self):
        r.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

class Card:
    def __init__(self,num,suite):
        self.num = num
        self.suite = suite
        self.value = self.calc_value()

    def calc_value(self):       #determine card's value for determining the hand's value
        try:
            value = int(self.num)
        except:
            if self.num == "A":
                value = 11
            else:
                value = 10
        return value

    def __repr__(self):
        return f'{self.num} of {self.suite}'

    def __add__(self,other):    #specifies that adding the card will add the value
        return other + self.value


if __name__ == "__main__":
    deck = Deck()
    for card in deck.cards:
        print(f'{card} with value {card.value}')
    print(len(deck.cards))