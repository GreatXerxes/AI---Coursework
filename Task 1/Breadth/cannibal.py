########################################################################
# cannibal (version for use with breadth first search)
########################################################################

from copy import deepcopy

def safe(state):
    # the side without the farmer needs check,
    # the other is safe
    
    # check left side
    statedict=state[1]
    canni, missi = statedict['left']['cannibal'],statedict['left']['missionary']

    unsafe_left = (missi == 1) and (canni >= 2*missi) # there's a miss, and more
                                            # c than miss

    # check right side
    canni, missi = statedict['right']['cannibal'],statedict['right']['missionary']
    unsafe_right = (missi == 1) and (canni >= 2*missi)
    #print "safe function right output", canni, missi

    return not unsafe_left and not unsafe_right
    
class Cannibal:

    def start(self):
        #the number on the first cell of tuple is a heuristic based on
        #total number of people on the left-bank
        return (6,{ 'left' : { 'cannibal' : 3,
                            'missionary' : 3 },
                 'right' : { 'cannibal' : 0,
                             'missionary' : 0 },
                 'boat' : 'left' })

    def goal(self, state):
        statedict=state[1]
        return statedict['right'] == { 'cannibal' : 3, 'missionary' : 3 }

    def succ(self, state):
        other_side = { 'left' : 'right', 'right': 'left' }
        max_boat = 2

        statedict=state[1]
        active_side = statedict['boat']
        canni = statedict[active_side]['cannibal']
        missi = statedict[active_side]['missionary']

        succlist=[]

        for total_travelers in range(1, max_boat+1): # how many can travel
            for canni_trav in range(0, total_travelers+1):
                missi_trav = total_travelers-canni_trav

                # cannot move more than there are on that side
                if canni_trav > canni:
                    print "canni_trav>canni triggered", canni_trav, canni
                    continue
                if missi_trav > missi:
                    print "missi_trav>missi triggered", missi_trav, missi
                    continue

                if (missi_trav+canni_trav)==0:
                    print "this should not happen"
                    continue

                new_statedict = deepcopy(statedict)

                new_statedict[active_side]['cannibal'] = statedict[active_side]['cannibal'] - canni_trav
                new_statedict[active_side]['missionary'] = statedict[active_side]['missionary'] - missi_trav

                new_statedict['boat'] = other_side[statedict['boat']]

                new_statedict[other_side[active_side]]['cannibal'] = statedict[other_side[active_side]]['cannibal'] + canni_trav
                new_statedict[other_side[active_side]]['missionary'] = statedict[other_side[active_side]]['missionary'] + missi_trav
                new_state=(new_statedict['left']['cannibal']+new_statedict['left']['missionary'], new_statedict)

                # after a trip, the new state is ok if no one gets eaten
                if safe(new_state):
                    succlist.append(new_state)


        return succlist
