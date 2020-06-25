
class Hand:
    def __init__(self,deck):
        self.deck = deck
        
        self.card1, self.card2 = self.deck.deal(), self.deck.deal()

        self.cards = {self.card1, self.card2}          #create set of the cards for quick comparison

        self.value = 0
        self.determine_value()      #go through cards and determine the value of the hand
    
        self.usable_ace = self.check_ace()  #returns boolean if the hand has an ace or not

    def check_ace(self):
        for card in self.cards:
            if card.num == "A":
                return True
        return False

    def determine_value(self):
        self.value = 0
        for card in self.cards:
            self.value += card.value
        if self.value > 21 and self.usable_ace:
            self.value -= 10

    def hit(self):          #have self.deck deal out a new card and add it to the set self.cards
        new_card = self.deck.deal()
        self.cards.update([new_card])
        self.usable_ace = self.check_ace()
        self.determine_value()

    def __repr__(self):
        return f'{self.cards}'

class HandD(Hand):
    def __init__(self,deck):
        super().__init__(deck)

        self.hidden = self.card1       #everything is the same except that Dealer has their cards additionally specified as hidden and visible
        self.visible_value = 0
        self.determine_visible_value()
        self.visible_cards = self.cards.copy()
        self.visible_cards.remove(self.hidden)

    def hit(self):          #have self.deck deal out a new card and add it to the set self.cards
        new_card = self.deck.deal()
        self.cards.update([new_card])
        self.visible_cards.update([new_card])   #this also makes it different

        self.usable_ace = self.check_ace()
        self.determine_value()
        self.determine_visible_value()      #slightly different than Hand.hit because needs to recalculate the visible value

    def determine_visible_value(self):
        self.visible_value = self.value - self.hidden.value