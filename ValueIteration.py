#Tinashe Mukundi Chitamba
#ML Assignment 2, part 1, value iteration

from gridpoint import gridPoint
import matplotlib.pyplot as plt

from Animate import generateAnimat


def main():
    
    width = 9
    height = 9
    start = [0,0]
    gamma = 0.8
    end = [3,4]
    grid = []



    #mines = [[3,4],[3,5],[4,5],[3,3],[3,2],[4,2]]
    #instatiating grid space and setting each point to zero
    for i in range(height):
        row = []
        for j in range(width):
            gridpoint = gridPoint(i,j,0,end[0],end[1],gamma)
            gridpoint.makePolicy()
            row.append(gridpoint)
        grid.append(row)

    #setting the values for end 
    grid[end[0]][end[1]].value = 150
    grid[end[0]][end[1]].isTerminal = True

    #iterating through the grid
    records = []
    for i in range(15):
        record = []
        for row in grid:
            recordrow = []
            for point in row:
                if point.isTerminal == False : #or point.isTerminal == True:
                    nextValues = []
                    for next in point.policies:
                        nextValues.append(point.getNextStateValue(grid[next[0]][next[1]]))
                    point.value = max(nextValues)
                recordrow.append(point.value)
                print(point.value,end=" ")
            record.append(recordrow)
            print()
        print()
        records.append(record)

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
    mines = [(3,4),(3,5),(4,5),(3,3),(3,2),(4,2)]  # Uncomment this to check out what mines will look like

	# We don't need a list of mine positions since our example doesn't have any
    opt_pol = [(0,0), (1, 0), (2, 0),(3,0), (3, 1),(3, 2),(3, 3),(3, 4)] # The above example has multiple valid optimal policies, this is just one of them.


    anim, fig, ax = generateAnimat(records, start_state, end_state, mines=mines, opt_pol=optpol, 
		start_val=-10, end_val=100, mine_val=150, just_vals=False, generate_gif=False,
		vmin = -10, vmax = 150)

    plt.show()

main()
