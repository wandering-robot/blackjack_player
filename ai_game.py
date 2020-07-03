from blackjack_cards import Deck, Card
from state import State, Q
from ai_hand import AI_Hand, AI_HandD


class AI_Game:
    """initialize an state action pair and determine the returns"""

    def __init__(self,agent,q0=None):
        self.deck = Deck()

        self.agent = agent
        self.q0 = q0

        #unpack this shit
        self.state, self.initial_action = self.q0 
        #instantiate the player's hand
        self.player = AI_Hand(self.state.player_value,self.state.usable_ace)     
        #instantiate the dealer's hand also dealing out the hidden card
        self.dealer = AI_HandD(self.state.dealer_visible_value,self.deck.deal())

        self.started = True         #used for round to determine using q action. if false use policy

        self.player_playing = True  #once a player stays they cannot play again

        self.visited_states = []        #to spread returns over all visited states

    def __repr__(self):
        return f'Player {self.player.value} Dealer {self.dealer.value}'

    def round(self):
        """Goes through a single round of hit/stay between the dealer and player and updates state data"""
        #player turn
        if self.started:
            self.started = False        #registers the game as started then immediately turns that value false
            if self.initial_action:
                card = self.deck.deal()
                self.player.value += card.value
                if card.is_ace:
                    self.player.usable_ace = True
            else:
                self.player.playing = False
        else:
            try:        #use this try except to handle states out of range aka obvious break                                        
                if self.agent.policy[self.state.data]:
                    card = self.deck.deal()
                    self.player.value += card.value
                    if card.is_ace:
                        self.player.usable_ace = True
                else:
                    self.player.playing = False
            except:
                self.player.playing = False
        #dealer turn
        if self.dealer.value < 17:
            card = self.deck.deal()
            self.dealer.value += card.value
            self.dealer.visible_value += card.value
        #allow people to reduce their scores by applying aces
        self.apply_ace()
        #check to see if anyone has bust by making bust people not _playing
        if self.player.value > 21:
            self.player.broke = True
            self.player.playing = False
        if self.dealer.value > 21:
            self.dealer.broke = True

    def update_state(self):
        try:
            self.state = self.agent.states[(self.player.value,self.dealer.visible_value,self.player.usable_ace)]
        except:
            self.state = None
        self.visited_states.append(self.state)      #add state to the list 
        

    def apply_ace(self):
        if self.player.usable_ace and self.player.value > 21:
            self.player.value -= 10
            self.player.usable_ace = False
        if self.dealer.usable_ace and self.dealer.value > 21:
            self.dealer.value -= 10
            self.dealer.usable_ace = False

    def end_game(self):
        if self.player.broke:
            return 0,self.visited_states
        elif self.dealer.broke:
            return 1,self.visited_states
        elif self.player.value > self.dealer.value:
            return 1,self.visited_states
        else:
            return 0,self.visited_states

    def play(self):
        """main loop for policy evaluation"""
        while True:
            self.round()
            if not(self.player.playing) and (self.dealer.value >= 17):
                break
            self.update_state()
        return self.end_game()
        