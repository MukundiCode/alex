#Tinashe Mukundi Chitamba
#ML Assignment 2, part 1, value iteration

from gridpoint import gridPoint


def main():
    
    width = 4
    height = 3
    start = [0.0]
    gamma = 0.8
    end = [3,4]
    grid = []

    #instatiating grid space and setting each point to zero
    for i in range(height):
        row = []
        for j in range(width):
            gridpoint = gridPoint(i,j,0,gamma)
            gridpoint.makePolicy()
            row.append(gridpoint)
        grid.append(row)

    #setting the values for end 
    grid[end[0]-1][end[1]-1].value = 100
    grid[end[0]-1][end[1]-1].isTerminal = True

    #iterating through the grid
    for i in range(5):
        for row in grid:
            for point in row:
                if point.isTerminal == False:
                    nextValues = []
                    for next in point.policies:
                        nextValues.append(point.getNextStateValue(grid[next[0]][next[1]]))
                    point.value = point.value + max(nextValues)
                print(point.value,end=" ")
            print()
        print()

main()
