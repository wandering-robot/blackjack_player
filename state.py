from hands import Hand, HandD
class Q:
    def __init__(self, state, action):
        self.state = state
        self.action = action

        self.value = 0

class State:
    def __init__(self,player_value,dealer_visible_value,usable_ace):
        self.player_value = player_value
        self.dealer_visible_value = dealer_visible_value
        self.usable_ace = usable_ace     #boolean if the hand has an ace or not



