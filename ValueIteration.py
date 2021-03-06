#Tinashe Mukundi Chitamba
#ML Assignment 2, part 1, value iteration

from gridpoint import gridPoint
import matplotlib.pyplot as plt
import numpy as np
from Animate import generateAnimat
import sys


def main():
    
    #setting defaults
    width = 12
    height = 12
    start = [0,0]
    gamma = 0.95
    end = [11,11]
    number_of_mines = 5

    if len(sys.argv) > 2:
        width = eval(sys.argv[1])
        height = eval(sys.argv[1])
        for i in range(len(sys.argv)):
            if sys.argv[i] == "-start":
                start = [int(sys.argv[i+1]),int(sys.argv[i+2])]
                print(start)
            elif sys.argv[i] == "-end":
                end = [int(sys.argv[i+1]),int(sys.argv[i+2])]
                print(end)
            elif sys.argv[i] == "-k":
                number_of_mines = eval(sys.argv[i+1])
            elif sys.argv[i] == "-gamma" :
                gamma = eval(sys.argv[i+1])

    grid = []
    records = []

    mines = generateRandomeMines(width,height,number_of_mines,start,end)
    print("Starting value itaration.")
    print("Starting point:",start)
    print("Ending point:",end)
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
    optpol = []
    if grid[start[0]][start[1]].getOptimal(optimal,grid,start[1],start[0]) == True:
        for opt in optimal:
            optpol.append((opt[1],opt[0]))
        print("Optimal policy: ",optpol)
    else:
        print("No optimal route found, please try again with more episodes, a higher learning rate, or less mines.")


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
            if prev[row][column] != current[row][column]:
                return False
    return True

main()
