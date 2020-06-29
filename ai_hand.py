
class AI_Hand:
    def __init__(self,value,usable_ace):
        self.value = value
        self.usable_ace = usable_ace

        self.playing = True
        self.broke = False
    
    def __repr__(self):
        return f'{self.value}:{self.usable_ace},{self.playing}'

class AI_HandD:
    def __init__(self,visible_value,hidden_card):
        self.visible_value = visible_value
        self.usable_ace = False
        if self.visible_value == 11:
            self.usable_ace = True
        self.hidden_card = hidden_card
        self.value = self.visible_value + self.hidden_card.value

        self.playing = True
        self.broke = False
        
    def __repr__(self):
        return f'{self.value}:{self.visible_value},{self.playing}'