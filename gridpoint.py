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
    def __init__(self,x,y,value,gamma):
        self.x = x
        self.y = y
        self.value = value
        self.gamma = gamma
        self.isTerminal = False

    def makePolicy(self):
        self.policies = []
        top = self.x -1
        bottom = self.x + 1
        left = self.y -1
        right = self.y +1
        if (top >= 0):
            self.policies.append([self.x-1,self.y])

        if (bottom <= 2):
            self.policies.append([self.x + 1,self.y])

        if (left >= 0):
            self.policies.append([self.x,self.y -1])

        if (right <= 3):
            self.policies.append([self.x,self.y+1])

    #gets the value of the next state, right now not including the reward of making the move 
    def getNextStateValue(self,nextState):
        return self.gamma * nextState.value