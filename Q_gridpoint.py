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
        else:
            self.policies.append(None)

        if (bottom <= self.endx):
            self.policies.append([self.x + 1,self.y])
        else:
            self.policies.append(None)

        if (left >= 0):
            self.policies.append([self.x,self.y -1])
        else:
            self.policies.append(None)

        if (right <= self.endy):
            self.policies.append([self.x,self.y+1])
        else:
            self.policies.append(None)

    #gets the value of the next state, right now not including the reward of making the move 
    def getNextStateValue(self,nextState):
        return (self.gamma*nextState.value)

    def getOptimal(self,optimal,grid,qtable):
        if self.isEnd == True:
            #optimal.append([self.x,self.y])
            return True
        else:
            nextAction = np.argmax(qtable[self.x,self.y])
            #print(nextAction,self.policies)
            #print(qtable[self.x,self.y])
            nextMove = self.policies[nextAction]
            if nextMove == None:
                return 
            for move in optimal:
                if move == nextMove :
                    print("No optimal route found")
                    print(move,optimal)
                    return
            #print(grid[nextMove[0]][nextMove[1]].value,next,sep=' ,')
            optimal.append(nextMove)
            return grid[nextMove[0]][nextMove[1]].getOptimal(optimal,grid,qtable)
            #cyclic route found
        #print("No possible route to end point")
        #return 

    def getOptimal_2(self,optimal,grid):
        if self.isEnd == True:
            #optimal.append([self.x,self.y])
            return
        else:
            #optimal.append([self.x,self.y])
            nextValues = []
            #finding the next optimal value
            for next in self.policies:
                if next != None:
                    nextValues.append(grid[next[0]][next[1]].value)

            maxValue = max(nextValues)
            for next in self.policies:
                if next != None:
                    if grid[next[0]][next[1]].value == maxValue:
                        print(grid[next[0]][next[1]].value,next,sep=' ,')
                        optimal.append(next)
                        return grid[next[0]][next[1]].getOptimal(optimal,grid)
            #cyclic route found
            print("No possible route to end point")
            return 


    def Q_getNextStateValue(self,nextState):
        return (self.gamma*nextState.value)

    def getNextAction(self,epsilon,grid,qtable):
        number = np.random.random()
        if number < epsilon:
            nextAction = np.argmax(qtable[self.x,self.y])
            #print(nextAction,self.policies)
            #print(qtable[self.x,self.y])
            nextMove = self.policies[nextAction]
            if nextMove == None:
                return -1
            if self.isEnd == False:
                self.value =  self.Q_getNextStateValue(grid[nextMove[0]][nextMove[1]])
            else:
                return -1
            #print(self.value)
            return [nextMove[0],nextMove[1],nextAction]

        else:
            rand = np.random.randint(len(self.policies))
            if not self.policies[rand] == None:
                if not grid[self.policies[rand][0]][self.policies[rand][0]].isTerminal:
                    if self.isEnd == False:
                        self.value = self.Q_getNextStateValue(grid[self.policies[rand][0]][self.policies[rand][0]])
                    #print(self.value)
                    return [self.policies[rand][0],self.policies[rand][0],rand]
                else:
                    self.value = self.Q_getNextStateValue(grid[self.policies[rand][0]][self.policies[rand][0]])
                    return -1
                #getting the positions of the 
            else:
                return -1

    def getNextAction2(self,epsilon,grid,qtable):
        number = np.random.random()
        if number < epsilon:
            nextAction = np.argmax(qtable[self.x,self.y])
            nextMove = self.policies[nextAction]
            self.value =  self.Q_getNextStateValue(grid[nextMove[0]][nextMove[1]])
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
                #self.value = self.Q_getNextStateValue(grid[self.policies[rand][0]][self.policies[rand][0]])
                return -1
            #getting the positions of the 

    def __str__(self) -> str:
        return str(self.x) + ":" + str(self.y)
                
