#Tinashe Mukundi Chitamba
#ML Assignment 2, part 1, value iteration

from gridpoint import gridPoint
import matplotlib.pyplot as plt
import numpy as np
from Animate import generateAnimat


def main():
    
    width = 30
    height = 30
    start = [2,3]
    gamma = 0.8
    end = [28,27]
    grid = []
    records = []

    mines = generateRandomeMines(width,height,150,start,end)
    #mines = [(3,5),(4,5),(3,3),(3,2),(4,2),(3,4)]
    #instatiating grid space and setting each point to zero
    record = []
    for i in range(height):
        row = []
        for j in range(width):
            gridpoint = gridPoint(i,j,-1,width-1,height-1,gamma)
            gridpoint.makePolicy()
            row.append(gridpoint)
        record.append(row)
        grid.append(row)
    #records.append(record)

    #setting the values for end 
    grid[end[0]][end[1]].value = 300
    grid[end[0]][end[1]].isTerminal = True
    #setting 0 values for the landmines
    for row in grid:
        for point in row:
            for mine in mines:
                if point.x == mine[1] and point.y == mine[0]:
                    point.isTerminal = True
                    point.value = -10
                    break

    #iterating through the grid
    converge = False
    index = 0
    #for i in range(20):
    while (converge == False):
        record = []
        for row in grid:
            recordrow = []
            for point in row:
                if point.isTerminal == False : #or point.isTerminal == True:
                    nextValues = []
                    for next in point.policies:
                        nextValues.append(point.getNextStateValue(grid[next[0]][next[1]]))
                    point.value = max(nextValues)
                    #print(nextValues,point.value,sep=" - ")
                recordrow.append(point.value)
                #print(point.value,end=" ")
            record.append(recordrow)
            #print()
        #print()
        #print(record)
        if index > 1:
            converge = is_converge(record,records[index-1])
        index = index + 1
        records.append(record)

    #finding the optimal policy
    optimal = []
    optimal.append(start)
    grid[start[0]][start[1]].getOptimal(optimal,grid,start[1],start[0])
    optpol = []
    for opt in optimal:
        optpol.append((opt[1],opt[0]))
    print("Optimal policy: ",optpol)


    start_state = (start[1], start[0])
    end_state = (end[1],end[0])


    anim, fig, ax = generateAnimat(records, start_state, end_state, mines=mines, opt_pol=optpol, 
		start_val=-10, end_val=100, mine_val=150, just_vals=False, generate_gif=False,
		vmin = -10, vmax = 150)

    plt.show()


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

main()
