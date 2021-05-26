#Tinashe Mukundi Chitamba
#The gridpoint class encapsulates the variables and methods used in the value iteration algorithm

class gridPoint:
    # Variables
    # x - x coordinate
    # y - y coordinate
    # int value - value of that grid point
    # boolean isTerminal - true if it is terminal point
    # policies [] - list of valid moves for this object

    #constructor
    def __init__(self,x,y,value,endx,endy,gamma):
        self.x = x
        self.y = y
        self.value = value
        self.gamma = gamma
        self.isTerminal = False
        self.endx = endx
        self.endy = endy

    def makePolicy(self):
        self.policies = []
        top = self.x -1
        bottom = self.x + 1
        left = self.y -1
        right = self.y +1
        if (top >= 0):
            self.policies.append([self.x-1,self.y])

        if (bottom <= self.endx):
            self.policies.append([self.x + 1,self.y])

        if (left >= 0):
            self.policies.append([self.x,self.y -1])

        if (right <= self.endy):
            self.policies.append([self.x,self.y+1])

    #gets the value of the next state, right now not including the reward of making the move 
    def getNextStateValue(self,nextState):
        return (self.gamma*nextState.value)

    def getOptimal(self,optimal,grid):
        if self.isTerminal == True:
            optimal.append([self.x,self.y])
            return
        else:
            optimal.append([self.x,self.y])
            nextValues = []
            #finding the next optimal value
            for next in self.policies:
                nextValues.append(grid[next[0]][next[1]].value)

            maxValue = max(nextValues)
            #print("Here ",maxValue)
            for next in self.policies:
                if grid[next[0]][next[1]].value == maxValue:
                    optimal.append(next)
                    return grid[next[0]][next[1]].getOptimal(optimal,grid)
                
