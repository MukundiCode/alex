#Tinashe Mukundi Chitamba
#ML Assignment 2, q learning part 
from numpy.random import random
from Q_gridpoint import gridPoint
import matplotlib.pyplot as plt
import numpy as np
from Animate import generateAnimat
import math


def main():
    #defining variables

    width = 30
    height = 30
    start = [0,0]
    gamma = 0.8
    epsilom = 0
    learning_rate = 0.4
    episodes = 200000
    end = [26,27]
    grid = []
    Qtable = np.zeros((width, height, 4))
    records = []

    #initilizing to zero
    #mines = [(3,5),(4,5),(3,3),(3,2)]#,(4,2),(3,4)]
    mines = generateRandomeMines(width,height,80,start,end)
    #mines = []
    #instatiating grid space and setting each point to zero
    record = []
    for i in range(height):
        row = []
        for j in range(width):
            gridpoint = gridPoint(i,j,1,width-1,height-1,gamma)
            gridpoint.makePolicy()
            row.append(gridpoint)
        record.append(row)
        grid.append(row)
    #records.append(record)

    #setting the values for end 
    grid[end[0]][end[1]].value = 200
    grid[end[0]][end[1]].isEnd = True
    #setting 0 values for the landmines
    for row in grid:
        for point in row:
            for mine in mines:
                if point.x == mine[1] and point.y == mine[0]:
                    point.isTerminal = True
                    point.value = -10
                    break

    #iterating through the grid with episodes
    logNumber = 1
    for episode in range(episodes):

        #getting the next random location
        record = []
        if (episode/episodes < 0.9):
            random1 = np.random.randint(0,width)
            random2 = np.random.randint(0,height)
        else:
            random1 = np.random.randint(0,int(width/2))
            random2 = np.random.randint(0,int(height/2))
        row_index = random1
        column_index = random2

        #while the chosen point is not terminal
        #print("*****************************************************")
        while(not is_terminal(grid,row_index,column_index)):
            #get the next action, returns points of action taken and index of action
            nextAction = grid[row_index][column_index].getNextAction(epsilom,grid,Qtable)
            #print(nextAction)
            if not nextAction == -1:
                #perform next action, move
                old_row = row_index
                old_column = column_index
                row_index = nextAction[0]
                column_index = nextAction[1]
                #print(old_row,old_column)
                #recieve reward and calculate temporal difference 
                reward = grid[row_index][column_index].value
                old_q_value = Qtable[old_row,old_column,nextAction[2]]
                temporal_difference = reward + (gamma * np.max(Qtable[row_index,column_index])) - old_q_value

                #update q table for prev state action pair 
                new_q_value = old_q_value + (learning_rate * temporal_difference)
                Qtable[old_row, old_column, nextAction[2]] = new_q_value
                #print(grid)
                #records.append(grid)
            else:
                break
        if episode%10000 == 0:
            for row in grid:
                recordrow = []
                for point in row:
                    recordrow.append(point.value)
                record.append(recordrow)
            records.append(record)
        #increasing epsilon linearly 
        gradient = 1/episodes
        epsilom = gradient*episode
        #learning_rate = 1/(1+episodes)
        if episode%10000 == 0:
            print("In the :",episode)

     #finding the optimal policy
    optimal = []
    optimal.append(start)
    grid[start[0]][start[1]].getOptimal(optimal,grid,Qtable)
    optpol = []
    for opt in optimal:
        optpol.append((opt[1],opt[0]))
    print("Optimal policy: ",optpol)


    start_state = (0, 0)
    end_state = (end[1],end[0])

    #mines = []
    #mines = [(3,4),(3,5),(4,5),(3,3),(3,2),(4,2)]  # Uncomment this to check out what mines will look like

	# We don't need a list of mine positions since our example doesn't have any
    opt_pol = [(0,0), (1, 0), (2, 0),(3,0), (3, 1),(3, 2),(3, 3),(3, 4)] # The above example has multiple valid optimal policies, this is just one of them.


    anim, fig, ax = generateAnimat(records, start_state, end_state, mines=mines, opt_pol=optpol, 
		start_val=-10, end_val=100, mine_val=150, just_vals=False, generate_gif=False,
		vmin = -10, vmax = 150)

    plt.show()
    #grid[start[0]][start[1]].getOptimal(optimal,grid,Qtable)

def is_terminal(grid,x,y):
    return grid[x][y].isTerminal


def generateRandomeMines(width,height,number,start,end):
    mines = []
    for mine in range(number):
        m = (np.random.randint(width),np.random.randint(height))
        #checking if mine is on start or stop
        while (m[1]==start[0] and m[0]==start[1]) or (m[1]==end[0] and m[0]== end[1]):
            m = (np.random.randint(width),np.random.randint(height))
        mines.append(m)
    #print("Random mines:",mines)
    return mines

def is_converge(prev,current):
    for row in range(len(prev)):
        for column in range(len(prev)):
            if int(prev[row][column]) != int(current[row][column]):
                return False
    return True

#def getOptimalPolicy(grid):


main()
