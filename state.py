
class Q:
    def __init__(self, state, action):
        self.state = state
        self.action = action

        self.action_word = self.determine_action
    
    def determine_action(self):
        if self.action:
            return 'hit'
        else:
            return 'stay'

    def __repr__(self):
        return f'q({self.state},{self.action_word})'

class State:
    def __init__(self,player_value,dealer_visible_value,usable_ace):
        self.player_value = player_value
        self.dealer_visible_value = dealer_visible_value
        self.usable_ace = usable_ace     #boolean if the hand has an ace or not

        self.data = (self.player_value,self.dealer_visible_value,self.usable_ace)

    def __repr__(self):
        return f's({self.player_value},{self.dealer_visible_value},{self.usable_ace})'

