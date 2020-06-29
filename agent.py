from ai_game import AI_Game
from state import Q,State
from blackjack_cards import Deck
from random import randint

class Agent:
    def __init__(self):
        self.states = {}
        for i in range(11,22):
            for j in range(11,22):
                for ace in [True,False]:
                    self.states[(i,j,ace)] = State(i,j,ace)     #create a dectionary for all states

        self.qs = {}
        for state in self.states.values():
            for a in [True,False]:
                self.qs[(state,a)] = Q(state,a)         #create a dictionary for all qs

        self.policy = {state:randint(0,1) for state in self.states}
        
        self.returns = {q:0 for q in self.qs}
        self.iteration = 1
        self.epsilon = 0.001
        self.done = False

    def update_average(self,q,result):
        """updates the average return for the given q"""
        a = 1/self.iteration
        b = 1 - a
        self.returns[q] = a * result + b * self.returns[q]

    def check_stability(self,new,old):
        return abs(new-old) < self.epsilon

    def eval(self):
        """main loop that enables policy evaluation"""
        while True:
            stable = True
            for q in agent.qs:
                game = AI_Game(agent,q)
                result = game.play() 
                old_result = self.returns[q]
                self.update_average(q,result)
                stable = self.check_stability(result,old_result)
            self.iteration += 1
            print(self.iteration)
            if stable:
                if self.iteration == 2:
                    self.done = True    #if all was identical from last iteration, should be optimal policy
                self.iteration = 1      #reset iterations to 1
                break

    def improve(self):
        """main loop for policy improvement"""
        for state in self.states.values():
            hit = self.qs[(state,True)].value
            stay = self.qs[(state,False)].value
            if hit > stay:
                self.policy[state] = 1
            else:
                self.policy[state] = 0

    def learn(self):
        """eval improve loop"""
        while not(self.done):
            self.eval()
            self.improve()

    def display(self):
        for state,action in self.policy.items():
            print(f'State {state}\t->\t{action}')


if __name__ == "__main__":
    agent = Agent()
    agent.learn()
    agent.display()