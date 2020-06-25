from blackjack_cards import Deck
from hands import Hand, HandD
from state import State

class Game:
    def __init__(self):
        self.deck = Deck()

        self.player = Hand(self.deck)

        self.dealer = HandD(self.deck)

        self.state = State(self.player.card1,self.player.card2,self.dealer.visible_value)

    def play(self):
        player_play = True
        dealer_play = True
        while player_play or dealer_play:
            print(f'Player has {game.player} valueing {game.player.value}')     
            print(f'Dealer has {game.dealer.visible_cards} with visible value {game.dealer.visible_value}')
            if input("hit?") == 'h':
                self.player.hit()
                if self.player.value > 21:
                    print("player breaks")
                    print(f'Player has {game.player} valueing {game.player.value}')     
                    print(f'Dealer has {game.dealer.cards} with visible value {game.dealer.value}')
                    break
            else:
                player_play = False
            if self.dealer.value < 17:
                self.dealer.hit()
                if self.dealer.value > 21:
                    print('dealer breaks')
                    print(f'Player has {game.player} valueing {game.player.value}')     
                    print(f'Dealer has {game.dealer.cards} with value {game.dealer.value}')
                    break
            else:
                dealer_play = False
            if self.player.value > self.dealer.value:
                print('Player wins')
            else:
                print('Dealer wins')
            print(f'Player has {game.player} valueing {game.player.value}')     
            print(f'Dealer has {game.dealer.cards} with value {game.dealer.value}')


if __name__ == "__main__":
    game = Game()
    game.play()


