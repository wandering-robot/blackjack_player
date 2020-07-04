from blackjack_cards import Card, Deck

class Savant:
    def __init__(self):

        self.policy = {}
        self.download_policy()

    def download_policy(self):
        with open('policy','r') as policy:
            for state_action in policy:
                state,action = state_action.rstrip().split(':')
                i,j,ace = state.split(',')
                self.policy[(int(i),int(j),ace=='True')] = int(action)

class HandP:
    def __init__(self):
        
        self.cards = []
        self.ace = False
        self.value = 0

        self.playing = True

    def calc_value(self):
        self.value = 0      #reset value
        for card in self.cards:
            self.value += card.value
        if self.value > 21 and self.ace:
            self.value -= 10

class HandD:
    def __init__(self):

        self.hidden_card = None
        self.vis_cards = []
        self.ace = False
        self.value = 0

    def calc_value(self):
        self.value = 0
        self.value += self.hidden_card.value
        for card in self.vis_cards:
            self.value += card.value
        if self.value > 21 and self.ace:
            self.value -= 10
            if self.hidden_card.value == 11:
                self.hidden_card.value = 1
            else:
                for card in self.vis_cards:
                    if card.value == 11:
                        card.value = 1
                        break

class Game:
    def __init__(self,savant):
        self.deck = Deck()

        self.player = HandP()
        self.player_init()

        self.dealer = HandD()
        self.dealer_init()

        self.savant = savant

    def player_init(self):
        for _ in range(2):
            card = self.deck.deal()
            if card.value == 11:
                self.player.ace = True
            self.player.cards.append(card)

    def dealer_init(self):
        card = self.deck.deal()
        if card.value == 11:
            self.dealer.ace = True
        self.dealer.hidden_card = card
        card = self.deck.deal()
        if card.value == 11:
            self.dealer.ace = True
        self.dealer.vis_cards.append(card)

    def apply_policy(self,state):
        if self.player.value < 12:
            return True
        elif self.player.value > 20:
            return False
        elif state[1] > 20:
            return False
        else:
            return self.savant.policy[state]

    def start(self):
        while True:
            self.player.calc_value()
            self.dealer.calc_value()
            if (self.player.value > 21 or not(self.player.playing)) and self.dealer.value >= 17:
                break
            else:
                self.round()
        return self.end_game()

    def round(self):
        state = (self.player.value,self.dealer.value-self.dealer.hidden_card.value,self.player.ace)
        if self.player.playing:
            if self.apply_policy(state):
                self.player.cards.append(self.deck.deal())
            else:
                self.player.playing = False
        if self.dealer.value < 17:
            self.dealer.vis_cards.append(self.deck.deal())

    def end_game(self):
        if self.player.value > 21:
            return 0
        elif self.dealer.value > 21:
            return 1
        elif self.player.value > self.dealer.value:
            return 1
        else:
            return 0

class Test:
    def __init__(self):
        self.savant = Savant()
        self.iters = 1
        self.average = 0
        self.go()

    def go(self):
        while True:
            game = Game(self.savant)
            result = game.start()
            self.update_average(result)
            print(self.average*100)

    def update_average(self,result):
        """updates the average return"""
        a = 1/self.iters
        b = 1 - a
        self.average = a * result + b * self.average
        self.iters += 1

if __name__ == "__main__":
    test = Test()


                
