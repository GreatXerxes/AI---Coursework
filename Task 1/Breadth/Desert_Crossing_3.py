########################################################################
# Desert Crossing (version for use with breadth first search)
########################################################################
from copy import deepcopy

def validState(state, x):
    #if state[0] == 4:
     #   return True

    fuelAtBase = state[2][state[0]-1] # Get the location of the truck

    if fuelAtBase == 0 and state[1]== 0: # Checking if the truck has fuel and if the base the truck is on has stored fuel
        return False
    else :
        return True

class Desert_Crossing_3:


    def start(self):
        return [0, 0, [99,0,0,0,0]] # [Position of truck, amount of fuel on truck, [Num fuel in 1st base, Num fuel in 2nd base, Num fuel in 3rd base, Num fuel in 4th base, Num fuel in last base]]

    def goal(self, state):
        if state[0] == 4: # Check if postion of truck is the same as the last base
            return True
        else:
            return False

    def succ(self, new_state):
        stateList = []
        state = deepcopy(new_state) # save state

        if state[0] == 0: # If truck position is in home base pick up max amount of fuel
            state[1] = 3

        for x in range(-state[1], state[1] + 1):# Possible bases, (x = num of base travelled)
            if state[0] + x in range(0, 4+1) and state[1] - abs(x) >= 0 and x <> 0:
                state[0] += x # Travel x bases
                state[1] -= abs(x) # Use up the fuel after travel

            #Dump Fuel at current base
            if state[0] in range(1, 4): # check if the truck is in the position of 1-3
                state[2][state[0]-1] += state[1]# Dump Fuel from the truck to base
                state[1]=0 # Set the truck to empty
                tempState = deepcopy(state) # Keep a copy of the current state to use for later
                for y in range(0, state[2][state[0]-1]+1): # Calculate possible fuel level after moving to destination, (y = fuel to load into truck)
                    if y > 3:
                        continue
                    state[2][state[0]-1] -= y # remove fuel from the current base
                    state[1] = y # Load fuel into the truck

                    if validState(state, x): # check if the move is valid/allowed
                        stateList.append(state)
                    state = deepcopy(tempState) #Undo all changes made to state in this loop

            else:
                if validState(state, x): # check if the move is valid/allowed
                    stateList.append(state)

            state = deepcopy(new_state) # save state

        return stateList




