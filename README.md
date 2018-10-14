# Escape-the-Maze
Using Reinforcement Learning the agent tries to escape a grid World avoiding the Bombs


The agent tries to reach the destination avoiding bombs and getting there with the least amount of penalties.
The environment is a 5*6 grid world which is filled with bombs,energy bars and the finish line.

In each step the agent gets a reward -1. If he falls into a Mine he get a reward -100. If he gets an energy bar he gets a reward +1. If he reaches the finish line he gets a reward +100.

Q-learning was implemented using Python. For the Visualization, Tkinter was used.


![alt text](https://github.com/Merkaster/Escape-the-Maze/blob/master/maze.png)

