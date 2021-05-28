#Tinashe Mukundi Chitamba
#ML Assignment 2, q learning part 
from numpy.random import random
from Q_gridpoint import gridPoint
import matplotlib.pyplot as plt
import numpy as np
from Animate import generateAnimat


def main():
    #defining variables

    width = 9
    height = 9
    start = [0,0]
    gamma = 0.8
    epsilom = 0.9
    learning_rate = 0.9
    episodes = 100
    end = [4,4]
    grid = []
    Qtable = np.zeros((width, height, 4))
    records = []

    #initilizing to zero
    mines = [(3,5),(4,5),(3,3),(3,2),(4,2),(3,4)]
    #mines = []
    #instatiating grid space and setting each point to zero
    record = []
    for i in range(height):
        row = []
        for j in range(width):
            gridpoint = gridPoint(i,j,0,width-1,height-1,gamma)
            gridpoint.makePolicy()
            row.append(gridpoint)
        grid.append(row)
    records.append(grid)

    #setting the values for end 
    grid[end[0]][end[1]].value = 150
    #grid[end[0]][end[1]].isTerminal = True
    #setting 0 values for the landmines
    for row in grid:
        for point in row:
            for mine in mines:
                if point.x == mine[0] and point.y == mine[1]:
                    point.isTerminal = True
                    point.value = -10
                    break

    #iterating through the grid with episodes
    for episode in range(episodes):

        #getting the next random location
        random1 = np.random.randint(0,9)
        random2 = np.random.randint(0,9)
        print(random1,random2)
        row_index = random1
        column_index = random2
        #while the chosen point is not terminal
        while(not is_terminal(grid,row_index,column_index)):
            #get the next action, returns points of action taken and index of action
            nextAction = grid[row_index][column_index].getNextAction(epsilom,grid)
            if not nextAction == -1:
                #perform next action, move
                old_row = row_index
                old_column = column_index
                row_index = nextAction[0]
                column_index = nextAction[1]

                #recieve reward and calculate temporal difference 
                reward = grid[row_index][column_index].value
                old_q_value = Qtable[old_row,old_column,nextAction[2]]
                temporal_difference = reward + (gamma * np.max(Qtable[row_index,column_index])) - old_q_value

                #update q table for prev state action pair 
                new_q_value = old_q_value + (learning_rate * temporal_difference)
                Qtable[old_row, old_column, nextAction[2]] = new_q_value
                #print(grid)
                records.append(grid)

     #finding the optimal policy
    optimal = []
    optimal.append(start)
    grid[start[0]][start[1]].getOptimal(optimal,grid)
    optpol = []
    for opt in optimal:
        optpol.append((opt[1],opt[0]))
    print("Optimal policy: ",optpol)


    start_state = (0, 0)
    end_state = (end[1],end[0])

    mines = []
    #mines = [(3,4),(3,5),(4,5),(3,3),(3,2),(4,2)]  # Uncomment this to check out what mines will look like

	# We don't need a list of mine positions since our example doesn't have any
    opt_pol = [(0,0), (1, 0), (2, 0),(3,0), (3, 1),(3, 2),(3, 3),(3, 4)] # The above example has multiple valid optimal policies, this is just one of them.


    anim, fig, ax = generateAnimat(records, start_state, end_state, mines=mines, opt_pol=optpol, 
		start_val=-10, end_val=100, mine_val=150, just_vals=False, generate_gif=False,
		vmin = -10, vmax = 150)

    plt.show()

def is_terminal(grid,x,y):
    return grid[x][y].isTerminal

main()
