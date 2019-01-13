from __future__ import print_function
from SearchAlgorithms.ClassicSearchAlgorithms import *
from SearchAlgorithms.BeyondClassicSearchAlgorithm import *
from copy import deepcopy
import numpy as np
import sys

class Problem():
    chess= [
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,0],
        [0,-1,0,0,0,0,0,0],
        [0,0,0,0,0,-1,0,0],
        [0,0,0,-1,0,0,0,0],
        [0,0,0,0,-1,0,0,0],
        [2,0,0,0,0,0,0,0],
        [0,0,0,0,2,0,0,0]
        ]
        #for item in chess:
          # print(item)
    for row in chess:
        for col in row:
            if col == 1:
                initial_state = (chess.index(row), row.index(col))
    wall = []
    
    for row in chess:
        for col in row:
            if col == -1:
                sare = (chess.index(row),row.index(col)) 
                wall.append(sare)
    '''             
    print(wall[0],wall[1],wall[2],wall[3])
    for item in wall:
        print("walls",item)
    '''   
     
    def initialState(self):    
        #print("initialstate",self.initial_state)
        return (0,5)    
    
    goals = []    
    def goal(self):
       #goals = [] 
       for row in self.chess:
        for col in row:
          if col == 2:
             g = (self.chess.index(row),row.index(col)) 
             self.goals.append(g)
       '''
        for item in self.goals:
            print("goals",item) 
       #print("hey youuu",self.goals[0][0],self.goals[0][1])
       '''
       return self.goals 

    def isGoalTest(self, state):
        #print("test",self.goal())
        if state in self.goal():
            return True
        else:
            return False
       # return state == self.goal()
    #def actions(self,state):
    def actions(self,state):
       #print("hey youuu",self.goals[0],self.goals[1]) 
       actions = []
       agent_row = state[0]
       #print(agent_row)
       agent_col = state[1]
       #print(agent_col)
       g1_row = self.goals[0][0]
       g1_col = self.goals[0][1]
       g2_row = self.goals[1][0]
       g2_col = self.goals[1][1]   
       '''for item in self.goals:
           print(item)
       print(g1_row,g1_col,g2_row,g2_col)  
       '''
       if agent_row > 1 :
            up = (agent_row-1,agent_col)
            if up not in self.goals:
                actions.append('U')

       if agent_row < g1_row or agent_row < g2_row :
            down = (agent_row + 1, agent_col)
            if down not in self.wall:
                actions.append('D') 

       if agent_col > 1:
            left = (agent_row, agent_col-1)
            if left not in self.wall: 
                actions.append('L')

       if agent_col < g1_col or agent_col < g2_col:
            right = (agent_row,agent_col+1)
            if right not in self.wall:      
                actions.append('R')
       
       '''
       for item in actions:
            print("in action func",item)
       '''  
       return actions
    
    def results(self,actions,state):
        states = []
        for action in actions:
            #print("first action",action)
            next_state = deepcopy(state)
            #print("next_state",next_state)
            next_state = list(next_state)
            state = list(state)
            if 'U' in action:
                next_state[0] = next_state[0] - 1
            elif 'D' in action:
                #print("hi down")
                next_state[0] = next_state[0] + 1
            elif 'L' in action:
                #print("hi left")                
                next_state[1] = next_state[1] - 1
            elif 'R' in action:
                next_state[1] = next_state[1] + 1
            #print("next_state after one ", next_state)
            states.append(tuple(next_state))
        #for item in states:
            #print(item)
        return states

    def step_cost(self, current_state, next_state):
        return 1
    
    def print_path(self, path):
        def find_direction(current_state, next_state):
            if current_state[0] == next_state[0] and current_state[1] > next_state[1]:
                print("L")
            elif current_state[0] == next_state[0] and current_state[1] < next_state[1]:
                print("R")
            elif current_state[0] > next_state[0] and current_state[1] == next_state[1]:
                print("U")
            elif current_state[0] < next_state[0] and current_state[1] == next_state[1]:
                print("D")

        print("Path:")
        for current_state, next_state in zip(path, path[1:]):
            find_direction(current_state, next_state)

    

p = Problem()
#p.actions(p.goal(),(0,5))
#p.results(p.actions(p.goal()),(0,5))
csa = ClassicSearchAlgorithm(p)
#bcsa = BeyondClassicSearchAlgorithm(p)

csa.graph_uniform_cost_search(p.initialState())
# csa.graph_breadth_first_search(p.initialState())
# csa.graph_bidirectional_search(p.initialState(), p.goal())
# csa.graph_uniform_cost_search(p.initialState())
# bcsa.graph_a_star(p.initialState())
