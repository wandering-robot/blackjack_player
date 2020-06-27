from hands import Hand, HandD
class Q:
    def __init__(self, state, action):
        self.state = state
        self.action = action

        self.action_word = self.determine_action

        self.value = 0
    
    def determine_action(self):
        if self.action:
            return 'hit'
        else:
            return 'stay'

    def __repr__(self):
        return f'{self.state},{self.action_word}'

class State:
    def __init__(self,player_value,dealer_visible_value,usable_ace):
        self.player_value = player_value
        self.dealer_visible_value = dealer_visible_value
        self.usable_ace = usable_ace     #boolean if the hand has an ace or not

    def __repr__(self):
        return f'({self.player_value},{self.dealer_visible_value},{self.usable_ace})'

