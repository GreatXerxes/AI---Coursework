########################################################################
# Desert Crossing (version for use with breadth first search)
########################################################################

from copy import deepcopy

class Desert_Crossing_2:

    def start(self):
        return [0, 0 , [0, 0, 0]]

    def goal(self,state):
        if state[0] == 4:
            return True
        return False


    def succ(self, state):
        MAX_FUEL = 99
        MAX_CARRIED = 3

        if state[0] == 0
            state[1] += MAX_CARRIED
            new_state = deepcopy(state)

        for sublist in state:
            if sublist[0]
        return

    
