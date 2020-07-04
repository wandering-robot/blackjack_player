from ai_game import AI_Game
from state import Q,State
from blackjack_cards import Deck
from random import randint

import atexit

class Agent:
    def __init__(self,new=False):
        self.states = {}
        for i in range(12,21):          #i is the player's actual value
            for j in range(2,21):       #j is the dealers visible value
                for ace in [True,False]:
                    # if j == 11 and ace == False:    #tweaking to get rid of impossible states
                    #     continue
                    # elif i == 12 and ace == True:
                    #     continue
                    self.states[(i,j,ace)] = State(i,j,ace)     #create a dectionary for all states

        self.qs = {}
        for state in self.states.values():
            for a in [True,False]:
                self.qs[(state,a)] = Q(state,a)         #create a dictionary for all qs

        if new:              #allow for user to create new policy if they want
            self.policy = {state:randint(0,1) for state in self.states.values()}
        else:
            self.policy = {}
            self.download_policy()
        
        self.returns = {q_key:0 for q_key in self.qs}   #returns
        self.returns_itr = {q_key:1 for q_key in self.qs}   #number of returns that q has seen

        self.iteration = 1
        self.done = False

    def update_average(self,q_key,result):
        """updates the average return for the given q"""
        a = 1/self.returns_itr[q_key]
        b = 1 - a
        self.returns[q_key] = a * result + b * self.returns[q_key]
        self.returns_itr[q_key] += 1

    def eval(self):
        """main loop that enables policy evaluation"""
        while self.iteration < 100:
            for q_key in self.qs:
                game = AI_Game(agent,q_key)
                result,visited_states = game.play()     #returns a tuple to be unpacked
                self.update_average(q_key,result)

                for state in visited_states:        #updates values for the visited states as well
                    if state != None:
                        state_q_key = (state,self.policy[state])
                        self.update_average(state_q_key,result)

            self.iteration += 1
        self.iteration = 1

    def improve(self):
        """main loop for policy improvement"""
        for state in self.states.values():
            hit = self.returns[(state,True)]
            stay = self.returns[(state,False)]
            if hit > stay:
                self.policy[state] = 1
            else:
                self.policy[state] = 0

    def learn(self):
        """eval improve loop"""
        iteration = 0
        while not(self.done):
            iteration += 1
            self.eval()
            self.improve()
            if iteration % 25 == 0:
                self.save_policy()
            print(iteration)
            
    def save_policy(self):
        with open('policy','w') as policy_file:
            for k,v in self.policy.items():
                policy_file.write(f'{k.player_value},{k.dealer_visible_value},{k.usable_ace}:{v}\n')


    def download_policy(self):
        with open('policy','r') as policy:
            for state_action in policy:
                state,action = state_action.rstrip().split(':')
                i,j,ace = state.split(',')
                self.policy[self.states[(int(i),int(j),ace == "True")]] = int(action)



if __name__ == "__main__":
    agent = Agent()
    atexit.register(agent.save_policy)
    agent.learn()
