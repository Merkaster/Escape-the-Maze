import numpy as np
import random
from copy import deepcopy
import tkinter as tk
from Visual import visualize

#Environment
BLANK = "b"
MINE = "m"
ROBOT = "r"
ENERGY = "e"
FINISH = "f"

Original_grid = [[ROBOT,BLANK,ENERGY,BLANK,BLANK,BLANK],
        [BLANK,MINE,BLANK,BLANK,MINE,BLANK],
        [BLANK,BLANK,ENERGY,BLANK,BLANK,ENERGY],
        [MINE,BLANK,BLANK,MINE,BLANK,BLANK],
        [BLANK,ENERGY,BLANK,BLANK,FINISH,BLANK]]

    

#ACTIONS
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

ACTIONS = [UP, DOWN, LEFT, RIGHT]

#Hyperparameters
random.seed(42)

N_STATES = 5
N_EPISODES = 50
MAX_EPISODES_STEPS = 100
MIN_ALPHA = 0.02

alphas = np.linspace(1, MIN_ALPHA, N_EPISODES)
gamma = 1
eps = 0.5

q_table = dict()


class State:
    
    def __init__(self, grid, robot_pos):
        self.grid = grid
        self.robot_pos = robot_pos
        
    def __eq__(self,other):
        return isinstance(other, State)and self.grid == other.grid and self.robot_pos == other.robot_pos
    
    def __hash__(self):
        return hash(str(self.grid) + str(self.robot_pos))
    
    def __str__(self):
        return f"State(grid={self.grid}, robot_pos={self.robot_pos})"


start_state = State(grid=Original_grid,robot_pos=[0,0])
#The starting position on the canvas
visualPos = [20,20]

def act(state,action):
    
    #Move the robot on the Grid depending on the action 
    def new_robot_pos(state,action):
        p = deepcopy(state.robot_pos)
        if action == UP:
            p[0] = max(0,p[0] -1)
        elif action == DOWN:
            p[0] = min(len(state.grid) -1,p[0] +1)
        elif action == RIGHT:
            p[1] = min(len(state.grid[0]) -1,p[1] +1)
        elif action == LEFT:
            p[1] = max(0,p[1] -1)
        else:
            raise ValueError(f"Unknown action {action}")
        
        return p
    
    p = new_robot_pos(state, action)
    grid_item = state.grid[p[0]][p[1]]
    
    
    new_grid = deepcopy(state.grid)
    
    #Check if the new position is Blank,has a Mine,has an Energy or if its the finish line and assign the rewards
    if grid_item == BLANK:
        reward = -1
        is_done = False
        old = state.robot_pos
        new_grid[old[0]][old[1]] = BLANK
        new_grid[p[0]][p[1]] = ROBOT
    elif grid_item == MINE:
        reward = -100
        is_done = True
    elif grid_item == ENERGY:
        reward = 1
        is_done = False
        old = state.robot_pos
        new_grid[old[0]][old[1]] = BLANK
        new_grid[p[0]][p[1]] = ROBOT
    elif grid_item == FINISH:
        reward = 100
        is_done = True
    elif grid_item == ROBOT:
        reward = -1
        is_done = False
    else:
        raise ValueError(f" Uknown grid item {grid_item}")
    
    
    return State(grid = new_grid,robot_pos=p), reward, is_done


def q(state,action = None):
    
    if state not in q_table:
        q_table[state] = np.zeros(len(ACTIONS))
    if action is None:
        return q_table[state]
    
    return q_table[state][action]

def choose_action(state,epoch):
    
    #Exploration vs Exploitation
    if random.uniform(0,1) < eps/epoch:
        return random.choice(ACTIONS)
    else:
        return np.argmax(q(state))

def train():
    
    
    for e in range(N_EPISODES):
        
        #Visualize the first and the last try
        if (e==1 or e==49):
            visualize(20, 20)
        state = start_state
        total_reward = 0
        alpha = alphas[e]
        
        for _ in range(MAX_EPISODES_STEPS):
            action = choose_action(state,e+1)
            next_state, reward, done = act(state, action)
            total_reward += reward
            
            q(state)[action] = q(state, action) + alpha * (reward + gamma *  np.max(q(next_state)) - q(state, action))
            
            state = next_state
            if(e == 1 or e==49):
                #Transfer the position of the robot to the Visualized grid
                visualize((state.robot_pos[1])*80+20, (state.robot_pos[0])*80+20)
            if done:
                break
            
        print(f"Episode {e + 1}: total reward -> {total_reward}")
    

train()
