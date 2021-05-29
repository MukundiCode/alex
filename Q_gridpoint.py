#Tinashe Mukundi Chitamba
#The gridpoint class encapsulates the variables and methods used in the value iteration algorithm
import numpy as np
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
        self.isEnd = False

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
        if self.isEnd == True:
            #optimal.append([self.x,self.y])
            return
        else:
            #optimal.append([self.x,self.y])
            nextValues = []
            #finding the next optimal value
            for next in self.policies:
                nextValues.append(grid[next[0]][next[1]].value)

            maxValue = max(nextValues)
            for next in self.policies:
                if grid[next[0]][next[1]].value == maxValue:
                    print(grid[next[0]][next[1]].value,next,sep=' ,')
                    optimal.append(next)
                    return grid[next[0]][next[1]].getOptimal(optimal,grid)

    def Q_getNextStateValue(self,nextState):
        return (self.gamma*nextState.value)

    def getNextAction(self,epsilon,grid):
        number = np.random.random()
        if number < epsilon:
            counter = 0
            maxValue = -1000
            action = 0
            for next in self.policies:
                if self.Q_getNextStateValue(grid[next[0]][next[1]]) > maxValue:
                    maxValue = self.Q_getNextStateValue(grid[next[0]][next[1]])
                    action = counter
                    nextMove = next
                counter = counter + 1
            if self.isEnd == False:
                self.value = maxValue
            else:
                return -1
            #print(self.value)
            return [nextMove[0],nextMove[1],action]

        else:
            rand = np.random.randint(len(self.policies))
            if not grid[self.policies[rand][0]][self.policies[rand][0]].isTerminal:
                if self.isEnd == False:
                    self.value = self.Q_getNextStateValue(grid[self.policies[rand][0]][self.policies[rand][0]])
                #print(self.value)
                return [self.policies[rand][0],self.policies[rand][0],rand]
            else:
                return -1
            #getting the positions of the 

    def __str__(self) -> str:
        return str(self.x) + ":" + str(self.y)
                
