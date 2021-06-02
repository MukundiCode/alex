Tinashe Mukundi Chitamba

src files:
1. gridpoint.py is an object for the gridpoint for the environment, and encapsulates the 
methods needed to get the next best move, get the optimal policy etc.
2. Q_gridpoint.py is another version of the gridpoint class in 1, but just has methods specific
to q learning
3. Valueiteration.py is the src file for question 1. To run it: python Valueiteration.py width height
it defaults to a grid size of 12 by 12 if no width and height are added. Gamma defaults to 0.95 
If no optimal policy is found just run it again with less mines
4. QLearning.py is the src file for question 2. I have added an additional option to set the number
of episodes you would want the agent to train for. It defaults at 100000, but thats would only
be necessary for larger grids, so you can set the episodes by -episodes e. 
If the agent doesn't get the best route, just try again with either a higher learning rate or
more episodes, eg for grids like 30 by 30, they would need at least 250 000 episodes 

If you get any error, maybe a recursion error or some index out of bounds, just try again, I've made 
sure to test the program enough, but I don't dismiss the possibility of there being some bugs.

Lastly, if in the unlikely case that the program doesn't run on linux, please just test and mark
using windows OS.

Thank You