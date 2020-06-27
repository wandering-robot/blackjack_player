from ai_game import AI_Game
from state import Q,State
from random import randint

class Agent:
    def __init__(self):
        self.states = {(i,j,ace):State(i,j,ace) for i in range(22) for j in range(11) for ace in [True, False]}
        self.qs = {(state,a):Q(state,a) for state in self.states for a in [True,False]]

        self.policy = {state:randint(0,1) for state in self.states}
        self.returns = {q:0 for q in self.qs}

    def learn(self):
        while True:
            game = AI_game(self)
            data = game.state_data
            state = self.states[data]
            a = randint(0,1)
            q =self.qs[(state,a)]


if __name__ == "__main__":
    agent = Agent()
    print(agent.qs)